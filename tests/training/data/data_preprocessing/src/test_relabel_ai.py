from asyncio import Semaphore
from pathlib import Path

import pandas as pd
import pytest
from datasets.preprocessing_scripts.scripts.relabel_ai import LLM, Audit
from datasets.preprocessing_scripts.scripts.relabel_ai import read_data, save_data

BASE_LOCATION: Path = Path(__file__).parent


@pytest.fixture
def semaphore() -> Semaphore:
    """Dummy semaphore"""
    return Semaphore(3)


@pytest.fixture
def no_col_df_path(tmp_path_factory):
    """Temporary mock file without the 'code' column"""
    # Define df
    df = pd.DataFrame({"complexity": ["123"]})
    # Create a temp file and directory
    file_path = tmp_path_factory.mktemp("data") / "no_col_df.csv"
    # Save
    save_data(df, file_path)
    return file_path


def test_audit_init_missing_code_column(mocker, no_col_df_path, semaphore) -> None:
    """Test for a raised exception if the columns doesn't exist"""
    # Create a mock since the classes are dependant upon external APIs
    mock_llm = mocker.Mock()

    # Test
    with pytest.raises(ValueError, match="Dataset must contain a 'code' column"):
        Audit(no_col_df_path, mock_llm, semaphore)


@pytest.fixture
def empty_df_path(tmp_path_factory):
    """Temporary mock empty file"""
    # Init df
    df = pd.DataFrame({"code": [], "complexity": []})
    # Create a temp file and directory
    fp = tmp_path_factory.mktemp("data") / "empty_df.csv"
    # Save
    save_data(df, fp)
    return fp


def test_audit_init_empty_dataframe(mocker, empty_df_path, semaphore) -> None:
    """Test for a raised exception if the dataframe is empty"""
    # Mock the LLM instance since the classes are dependant upon external APIs
    mock_llm = mocker.Mock()

    # Test
    with pytest.raises(ValueError, match="Dataset is empty"):
        Audit(empty_df_path, mock_llm, semaphore)


@pytest.mark.asyncio
async def test_process_requests(mocker, dummy_source_file_path, semaphore) -> None:
    """Test processing API requests"""
    # Create a mock since the classes are dependant upon external APIs
    mock_llm = mocker.Mock()

    # Create audit instance with mocked LLM and semaphore
    audit = Audit(dummy_source_file_path, mock_llm, semaphore)

    # Mock send requests to return certain responses
    mock_llm.send_requests = mocker.AsyncMock(side_effect=["O(n)", None, "O(1)"])

    # Test
    got: list[str | None] = await audit.process_requests("test instructions")

    # Verify
    assert got == ["O(n)", None, "O(1)"]
    assert mock_llm.send_requests.call_count == 3


@pytest.fixture
def responses() -> list[str]:
    """Mock responses from an LLM API"""
    return ["O(n)", "O(nlogn)", "O(1)"]


def test_process_responses(mocker, responses, dummy_source_file_path, semaphore) -> None:
    """Test request processing functionality"""
    # Create mocks since the classes are dependant upon external APIs
    mock_llm = mocker.Mock(LLM)
    # Mock the prefix of the name of the column where the LLM's decisions are stored
    mock_llm.model = "test_name"

    # Define audit
    audit = Audit(dummy_source_file_path, mock_llm, semaphore)

    # Test
    audit.process_responses(responses)
    got: dict[str, list[str | None]] = audit.llm_decisions

    expected: dict[str, list[str]] = {"test_name_decision": ["O(n)", "O(nlogn)", "O(1)"]}

    assert got == expected


@pytest.fixture
def expected_saved_data() -> pd.DataFrame:
    """Dummy expected data for the test_save_data_to_review"""
    return pd.DataFrame(
        {
            "code": [
                "class Solution(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        def backtracking(curr, cnt, result): \n# Testing testing 123\n\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            for i, c in enumerate(cnt):\n                if c == 0 or (not curr and i == 0) or (len(curr) == k-1 and i%2 != 0):\n                    continue\n                cnt[i] -= 1\n                curr.append(i)\n                backtracking(curr, cnt, result)\n                curr.pop()\n                cnt[i] += 1\n\n        cnt = [0]*10\n        for d in digits:\n            cnt[d] += 1\n        result = []\n        backtracking([], cnt, result)\n        return result",
                "class Solution2(object):\n    def findEvenNumbers(self, digits):\n\n\n\n\n\n\n\n        result, cnt = [], collections.Counter(digits)\n        for i in range(1, 10):\n            for j in range(10):\n                for k in range(0, 10, 2):\n                    if cnt[i] > 0 and cnt[j] > (j == i) and cnt[k] > (k == i) + (k == j):\n                        result.append(i*100 + j*10 + k)\n        return result",
                "class Solution3(object):\n    def findEvenNumbers(self, digits):\n        k = 3\n        \n        def backtracking(curr, dummy, result):\n            if len(curr) == k:\n                result.append(reduce(lambda x, y: x*10+y, curr))\n                return\n            node = dummy.right\n            while node:\n                if (not curr and node.val[0] == 0) or (len(curr) == k-1 and node.val[0]%2 != 0):\n                    node = node.right\n                    continue\n                node.val[1] -= 1\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node.right\n                    if node.right:\n                        node.right.left = node.left\n                curr.append(node.val[0])\n                backtracking(curr, dummy, result)\n                curr.pop()\n                if node.val[1] == 0:\n                    if node.left:\n                        node.left.right = node\n                    if node.right:\n                        node.right.left = node\n                node.val[1] += 1\n                node = node.right\n\n        prev = dummy = Node()\n        for digit, cnt in sorted(map(list, iter(collections.Counter(digits).items()))):\n            prev.right = Node(val=[digit, cnt], left=prev)\n            prev = prev.right\n        result = []\n        backtracking([], dummy, result)\n        return result",
            ],
            "complexity": ["O(n)", "# Time:  O(n), n is 10^3", "# Time:  O(1) ~ O(n), n is 10^3"],
            "test_name_decision": ["O(n)", "O(nlogn)", "O(1)"],
        }
    )


def test_save_data_to_review(
    mocker, dummy_source_file_path, dummy_target_file_path, expected_saved_data, semaphore
) -> None:
    """Test save_data method that joins the 'LLM_decision' column with the original data"""
    # Mock class params and model for reproduction
    mock_llm = mocker.Mock(LLM)
    mock_llm.model = "test_name"

    # Test the joining logic
    audit = Audit(dummy_source_file_path, mock_llm, semaphore)
    # Dummy responses
    audit.llm_decisions = {"test_name_decision": ["O(n)", "O(nlogn)", "O(1)"]}

    # Test for file existence
    audit.save_data_to_review(dummy_target_file_path)
    assert dummy_target_file_path.exists()

    # Test for file contents
    got: pd.DataFrame = read_data(dummy_target_file_path)
    assert got.equals(expected_saved_data)

    # Delete file
    dummy_target_file_path.unlink(missing_ok=True)

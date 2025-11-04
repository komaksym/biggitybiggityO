from .data import generate_prompt, label2id
from transformers import AutoTokenizer 
from pathlib import Path
from peft import PeftModel
from .model import set_model
import re
from .configs.config import checkpoint

BASE_LOCATION: Path = Path(__file__).parent


def data_preprocessing(inputs):
    """Preprocesses data and applies instruction prompt"""

    def remove_comments(code_sample: str) -> str:
        """Remove in-code comments."""

        return re.sub(
            r"(#.+?$)|([\"']{3,}.+?[\"']{3,})",
            "",
            code_sample,
            flags=re.MULTILINE | re.DOTALL,
        )

    def strip_empty_lines(code_sample: str) -> str:
        """
        Remove consecutive empty lines and keep only 1 between code lines.
        """

        filtered_code: list[str] = []

        for line in code_sample.split("\n"):
            line: str = line.rstrip()

            if line == "":
                # If previous line is not another empty line
                if filtered_code and filtered_code[-1] != "":
                    filtered_code.append(line)
                else:
                    continue
            else:
                filtered_code.append(line)

        return "\n".join(filtered_code)
    
    inputs = remove_comments(inputs)
    inputs = strip_empty_lines(inputs)
    print(inputs)
    


def predict(input):
    """Predict and output the class"""

    pass


def main():
    ## Path for the pretrained model
    #pretrained_path = (
        #BASE_LOCATION.parents[1] / "models/best_model/deepseek-ai/deepseek-coder-1.3b-base/"
    #)

    ## Loading pretrained tokenizer and model
    #tokenizer = AutoTokenizer.from_pretrained(pretrained_path)
    ## Base model
    #base_model = set_model(checkpoint, tokenizer)
    ## Load pretrained LoRA adapters on top
    #model = PeftModel.from_pretrained(base_model, pretrained_path, dtype="auto", device_map="auto")

    ## Enable model eval mode to turn off dropout, grads, etc.
    #model.eval()
    
    inputs = """"
    # Sum of a Fibonacci series up to the nth term
def o2n_fibonacci(n):
'''Comments'''
    if n<2: # Comments
        return n #Comments	
    print("hello")
    return o2n_fibonacci(n-1) + o2n_fibonacci(n-2)
    """
    data_preprocessing(inputs)


if __name__ == "__main__":
    main()


import json



def extract_tusimple_data(data_path: str, ground_truth_path: str, raw_file_substring: str) -> None:
    """
    Extracts TuSimple label entries where the 'raw_file' contains a given substring.

    Args:
        data_path (str): Path to the full TuSimple JSONL file.
        ground_truth_path (str): Path to save the filtered JSONL.
        raw_file_substring (str): A string to match in the 'raw_file' field (e.g., sequence or full filename).
    """
    try:
        with open(data_path, "r") as f:
            matches = [
                json.loads(line) for line in f
                if raw_file_substring in line
            ]

        with open(ground_truth_path, "w") as f_out:
            for entry in matches:
                f_out.write(json.dumps(entry) + "\n")

        print(f"✅ Found and saved {len(matches)} matching label(s) containing '{raw_file_substring}'")

    except Exception as e:
        print(f"❌ Error: {e}")


from pathlib import Path

target_substring = input("Enter target substring: ")
replacement_substring = input("Enter replacement substring: ")
target_path = Path(input("Enter path: "))

for path in target_path.rglob("*"):
    if path.suffix == ".py":

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            script = f.read()
        
        new_script = script.replace(target_substring, replacement_substring)
        
        if new_script != script:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_script)
            
            print(f"Updated: {path}")

import re

def clean_phone_number(phone):
    digits = ''.join(filter(str.isdigit, phone))
    return digits[:20] if digits else '9999999999'

def fix_phones_in_insert_block(block, table_name, phone_index):
    def replace_values(match):
        values = [v.strip() for v in match.group(1).split(",")]
        phone_raw = values[phone_index].strip("'").strip()
        fixed_phone = clean_phone_number(phone_raw)
        values[phone_index] = f"'{fixed_phone}'"
        return "(" + ", ".join(values) + ")"
    
    pattern = rf"(INSERT INTO {table_name} .*?VALUES\s*)(.+?);"
    match = re.search(pattern, block, re.DOTALL | re.IGNORECASE)
    if not match:
        return block

    header, values_block = match.groups()
    fixed_values = re.sub(r"\(([^()]+?)\)", replace_values, values_block)
    return block.replace(match.group(0), header + fixed_values + ";")

# Load your original .sql file
input_path = "banking_system_full_final_corrected.sql"
output_path = "banking_system_full_final_cleaned.sql"

with open(input_path, "r", encoding="utf-8") as file:
    content = file.read()

# Fix customer and employee phone numbers
content = fix_phones_in_insert_block(content, "customers", 3)
content = fix_phones_in_insert_block(content, "employees", 3)

# Save the cleaned SQL file
with open(output_path, "w", encoding="utf-8") as file:
    file.write(content)

print(f"✅ Cleaned phone numbers. Output saved to: {output_path}")
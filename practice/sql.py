import re
from collections import defaultdict

input_file = "company_hr_full_dump.sql"       # your original file
output_file = "company_hr_full_dump_batch.sql"  # output file

# Pattern to extract insert info
insert_pattern = re.compile(r"^INSERT INTO (\w+) \((.+?)\) VALUES \((.+?)\);$", re.IGNORECASE)

# Store results
create_statements = []
insert_batches = defaultdict(lambda: {"columns": None, "values": []})
other_statements = []

# Read input file
with open(input_file, "r", encoding="utf-8") as f:
    current_create = ""
    in_create = False
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith("CREATE TABLE"):
            in_create = True
            current_create = line
        elif in_create:
            current_create += " " + line
            if line.endswith(";"):
                create_statements.append(current_create)
                in_create = False
        elif line.startswith("INSERT INTO"):
            match = insert_pattern.match(line)
            if match:
                table, columns, values = match.groups()
                insert_batches[table]["columns"] = columns
                insert_batches[table]["values"].append(f"({values})")
        else:
            other_statements.append(line)

# Write to output file
with open(output_file, "w", encoding="utf-8") as f:
    # Header and other non-inserts
    for stmt in other_statements:
        f.write(stmt + "\n\n")

    # CREATE TABLE statements
    for stmt in create_statements:
        f.write(stmt + "\n\n")

    # Batched INSERTS
    for table, data in insert_batches.items():
        values = ",\n".join(data["values"])
        f.write(f"INSERT INTO {table} ({data['columns']}) VALUES\n{values};\n\n")

print(f"✅ Conversion complete! Output saved to: {output_file}")
# Vendor Language Engine - Master Version (All-in-One)

memory = {}

def execute_action(action_str):
    action_str = action_str.strip()
    if action_str.startswith("show "):
        print(f"Vendor Output: {action_str.replace('show ', '').strip()}")
    elif action_str.startswith("காட்டு "):
        print(f"Vendor Output (தமிழ்): {action_str.replace('காட்டு ', '').strip()}")

def run_vendor(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
        for line_number, line in enumerate(lines, start=1):
            command = line.strip()
            if not command: continue
            cmd_lower = command.lower()

            # 1. Output / காட்டு
            if command.startswith("show ") or command.startswith("காட்டு "):
                execute_action(command)

            # 2. Variables / பதிவு
            elif cmd_lower.startswith("set ") and " to " in cmd_lower:
                var, val = cmd_lower.replace("set ", "").split(" to ")
                memory[var.strip()] = int(val.strip()) if val.strip().isdigit() else val.strip()
            elif command.startswith("பதிவு ") and "=" in command:
                var, val = command.replace("பதிவு ", "").split("=")
                memory[var.strip()] = int(val.strip()) if val.strip().isdigit() else val.strip()

            # 3. Math / கணிதம்
            elif cmd_lower.startswith("add ") and " and " in cmd_lower:
                v1, v2 = cmd_lower.replace("add ", "").split(" and ")
                if v1.strip() in memory and v2.strip() in memory:
                    print(f"Vendor Math: {v1.strip()} + {v2.strip()} = {memory[v1.strip()] + memory[v2.strip()]}")
            elif " மற்றும் " in command and " ஐ கூட்டு" in command:
                v1, v2 = command.replace(" ஐ கூட்டு", "").split(" மற்றும் ")
                if v1.strip() in memory and v2.strip() in memory:
                    print(f"Vendor கணிதம்: {v1.strip()} + {v2.strip()} = {memory[v1.strip()] + memory[v2.strip()]}")

            # 4. Conditions (If/Else) / நிபந்தனைகள்
            elif cmd_lower.startswith("if ") and " then " in cmd_lower:
                condition, action = command[3:].split(" then ", 1)
                var, limit = condition.split(">")
                if var.strip() in memory and memory[var.strip()] > int(limit.strip()):
                    execute_action(action)
            elif " என்றால் " in command and ">" in command:
                condition, action = command.split(" என்றால் ", 1)
                var, limit = condition.split(">")
                if var.strip() in memory and memory[var.strip()] > int(limit.strip()):
                    execute_action(action)

            # 5. Loops / சுழற்சிகள்
            elif cmd_lower.startswith("repeat ") and " times " in cmd_lower:
                times, action = command[7:].split(" times ", 1)
                for _ in range(int(times.strip())): execute_action(action)
            elif " முறை திரும்பு " in command:
                times, action = command.split(" முறை திரும்பு ", 1)
                for _ in range(int(times.strip())): execute_action(action)

    except FileNotFoundError:
        print("Error: test.ven file not found!")

print("--- Starting Vendor Master Engine ---")
run_vendor("test.ven")
print("--- Execution Completed ---")
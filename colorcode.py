# Variable Setup:
color = [0, 0, 0, float(0.0)]
check = True
print("""
+==== RGB to monke converter ====+
Mode 1: Convert RGB to Monke
Mode 2: Convert Monke to RGB
Mode 3: Convert HEX to RGB

      """)

# Asks which mode to use
mode = int(input("Mode: "))
if mode == 1 or mode == 2:
    color[0] = int(input("Red Value: "))
    color[1] = int(input("Green Value: "))
    color[2] = int(input("Blue Value: "))
elif mode == 3:
    hex_code = str(input("HEX Code: "))

def RgbToMonke():
    global check
      # Checks if value is valid
    for i in range(3):
        if color[i] > 255:
            check = False
            print("Each Color Value can be 255 at max.")
            break

      # Converts by using the rule of three method
    if check:
        for i in range(3):
            color[3] = color[i] / 255
            print(int(color[3] * 9))

def MonkeToRbg():
    global check
      # Checks if value is valid
    for i in range(3):
        if color[i] > 9:
            check = False
            print("Each Color Value can be 9 at max.")
            break
      # Converts by using the rule of three method
    if check:
        for i in range(3):
            color[3] = color[i] / 9
            print(int(color[3] * 255))

def HexToRgb():
    global r, g, b, hex_code
      #Had to use chatgpt cause wtf is this shit
    hex_code = hex_code.lstrip('#')
    color[0] = int(hex_code[0:2], 16)
    color[1] = int(hex_code[2:4], 16)
    color[2] = int(hex_code[4:6], 16)

if mode == 1:
    RgbToMonke()
elif mode == 2:
    MonkeToRbg()
elif mode == 3:
    HexToRgb()
    RgbToMonke()
else:
    print(f"{mode} is not a valid Mode!")

temperature = 39.1
# label = "High" else "Normal" if temperature >= 38 else "Low" => buggy
label = "Normal" if temperature >= 38 else "Low"
print("Label:", label)

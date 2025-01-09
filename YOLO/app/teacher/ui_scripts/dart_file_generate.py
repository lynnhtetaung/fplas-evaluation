import os
import random

from flask import Flask


app = Flask(__name__)

# Folder to save generated Flutter files
dart_files_output_dir = os.path.join(app.static_folder, 'dart_files_output')

# Ensure the generated_ui folder exists
os.makedirs(dart_files_output_dir, exist_ok=True)

# Define UI components
colors = ["Colors.blue", "Colors.green", "Colors.red", "Colors.orange", "Colors.purple"]
text_styles = [
    "TextStyle(fontSize: 16, fontWeight: FontWeight.bold)",
    "TextStyle(fontSize: 20, fontStyle: FontStyle.italic)",
    "TextStyle(fontSize: 14, color: Colors.grey)",
]
button_labels = ["Submit", "Cancel", "Next", "Back"]
dropdown_options = [["Option 1", "Option 2", "Option 3"], ["A", "B", "C"], ["Yes", "No"]]

# Generate random Flutter UI source code
def generate_flutter_code(index):
    title = f"Mock UI {index}"
    app_bar_color = random.choice(colors)
    button_label = random.choice(button_labels)
    dropdown_items = random.choice(dropdown_options)
    text_style = random.choice(text_styles)

    dropdown_code = "\n".join(
        [f"DropdownMenuItem(value: '{opt}', child: Text('{opt}'))," for opt in dropdown_items]
    )

    return f"""
import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {{
  const MyApp({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('{title}'),
          backgroundColor: {app_bar_color},
        ),
        body: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Choose an option:',
                style: {text_style},
              ),
              const SizedBox(height: 10),
              DropdownButton<String>(
                items: [
                  {dropdown_code}
                ],
                onChanged: (value) {{}},
                hint: const Text('Select one'),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                onPressed: () {{}},
                child: const Text('{button_label}'),
              ),
            ],
          ),
        ),
      ),
    );
  }}
}}
"""

# Generate multiple Flutter files
num_files = 50  # Change this to 100 for more files
for i in range(1, num_files + 1):
    flutter_code = generate_flutter_code(i)
    file_path = os.path.join(dart_files_output_dir, f"mock_ui_{i}.dart")
    with open(file_path, "w") as f:
        f.write(flutter_code)

print(f"Generated {num_files} Flutter UI files in '{dart_files_output_dir}'.")

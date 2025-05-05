import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  bool isUniversityChecked = true;
  bool isCatChecked = false;
  bool isStationChecked = false;

  String selectedImage = 'assets/university.jpg';

  void updateChecked(String label) {
    setState(() {
      if (label == 'University') {
        isUniversityChecked = true;
        isCatChecked = false;
        isStationChecked = false;
        selectedImage = 'assets/university.jpg'; // Update image to university
      } else if (label == 'Cat') {
        isUniversityChecked = false;
        isCatChecked = true;
        isStationChecked = false;
        selectedImage = 'assets/cat.png';
      } else if (label == 'Station') {
        isUniversityChecked = false;
        isCatChecked = false;
        isStationChecked = true;
        selectedImage = 'assets/university.jpg'; // Update image to university
      }
    });
  }

  @override
  Widget build(BuildContext context) {

    const title = 'Exercise 5 - Checkbox';

    return MaterialApp(
      title: title,
      home: Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black, // Border color
            width: 10.0, // Border width
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text(title),
            backgroundColor: Colors.blue,
            titleTextStyle: TextStyle(
              color: Colors.white, // AppBar title text color
              fontWeight: FontWeight.bold, // AppBar title text weight
              fontSize: 30, // AppBar title text size
            ),
          ),
          body: Padding(
            padding: const EdgeInsets.all(20.0),
            child: Column(
              children: <Widget>[
                // Display the image at the top
                Center(
                  child: Image.asset(
                    selectedImage,
                    height: 300, // Adjust the image size as needed
                    width: 300,
                  ),
                ),
                const SizedBox(height: 20),
                // Checkbox List with adjusted font size, color, and weight
                CheckboxListTile(
                  title: const Text(
                    'University',
                    style: TextStyle(
                      fontSize: 24.0, // Increased font size
                      color: Colors.red, // Changed font color to red
                      fontWeight: FontWeight.bold, // Set font weight to bold
                    ),
                  ),
                  value: isUniversityChecked,
                  onChanged: (bool? value) {
                    if (value != null && value) {
                      updateChecked('University');
                    }
                  },
                ),
                CheckboxListTile(
                  title: const Text(
                    'Cat',
                    style: TextStyle(
                      fontSize: 24.0, // Increased font size
                      color: Colors.black, // Changed font color to green
                      fontWeight: FontWeight.w600, // Medium boldness
                    ),
                  ),
                  value: isCatChecked,
                  onChanged: (bool? value) {
                    if (value != null && value) {
                      updateChecked('Cat');
                    }
                  },
                ),
                CheckboxListTile(
                  title: const Text(
                    'Station', // Change this text to 'University'
                    style: TextStyle(
                      fontSize: 24.0, // Increased font size
                      color: Colors.black, // Changed font color to black
                      fontWeight: FontWeight.w600, // Normal weight
                    ),
                  ),
                  value: isStationChecked,
                  onChanged: (bool? value) {
                    if (value != null && value) {
                      updateChecked('Station');
                    }
                  },
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  int _selectedIndex = 0;

  // List of widgets for each page
  final List<Widget> _pages = [
    HomePage(),
    BusinessPage(),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Container(
        // Apply border for the entire app
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black, // Border color
            width: 10, // Border width
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text('Exercise 4 - BottomNavigationBar'),
            backgroundColor: Colors.blue,
            titleTextStyle: TextStyle(
                color: Colors.white, // AppBar title text color
                fontWeight: FontWeight.bold, // AppBar title text weight
                fontSize: 30, // AppBar title text size
            ),
          ),
          body: _pages[_selectedIndex],
          bottomNavigationBar: BottomNavigationBar(
            currentIndex: _selectedIndex,
            onTap: _onItemTapped,
            items: const [
              BottomNavigationBarItem(
                icon: Icon(Icons.home),
                label: 'Home',
              ),
              BottomNavigationBarItem(
                icon: Icon(Icons.business),
                label: 'Business',
              ),
            ],
            selectedItemColor: Colors.red, // Color for the selected item
            unselectedItemColor: Colors.grey, // Color for unselected items
            selectedLabelStyle: TextStyle(
              fontWeight: FontWeight.bold, // Make text bold
              color: Colors.red, // Text color for selected item
            ),
            type: BottomNavigationBarType.fixed,
          ),
        ),
      ),
    );
  }
}

// Home Page Widget
class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.home, size: 100, color: Colors.blue),
          const Text('Home Page', style: TextStyle(fontSize: 40)),
          ElevatedButton(
            onPressed: () {
              // Add your action here
            },
            child: const Text(
              'Go to Home',
              style: TextStyle(fontSize: 30), // フォントサイズを30に設定
            ),
          ),
        ],
      ),
    );
  }
}

// Business Page Widget
class BusinessPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.person, size: 100, color: Colors.orange),
          const Text('Business Page', style: TextStyle(fontSize: 25)),
          ElevatedButton(
            onPressed: () {
              // Add your action here
            },
            child: const Text('Come to Business'),
          ),
        ],
      ),
    );
  }
}

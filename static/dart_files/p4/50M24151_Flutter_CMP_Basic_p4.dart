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
  final List<Widget> _pages = [];

  @override
  void initState() {
    super.initState();

    // Initialize the pages, passing the navigation callback
    _pages.addAll([
      HomePage(navigateToHome: () => _onItemTapped(0)),
      BusinessPage(navigateToHome: () => _onItemTapped(0)),
    ]);
  }

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
            titleTextStyle: const TextStyle(
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
            selectedLabelStyle: const TextStyle(
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
  final VoidCallback navigateToHome;

  const HomePage({required this.navigateToHome});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.home, size: 100, color: Colors.blue),
          const Text(
            'Home Page',
            style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: navigateToHome,
            child: const Text(
              'Go to Home',
              style: TextStyle(fontSize: 30),
            ),
          ),
        ],
      ),
    );
  }
}

// Business Page Widget
class BusinessPage extends StatelessWidget {
  final VoidCallback navigateToHome;

  const BusinessPage({required this.navigateToHome});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.person, size: 100, color: Colors.orange),
          const Text(
            'Business Page',
            style: TextStyle(fontSize: 25),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: navigateToHome,
            child: const Text('Go to Home'),
          ),
        ],
      ),
    );
  }
}

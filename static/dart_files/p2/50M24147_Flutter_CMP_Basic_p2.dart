import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const title = 'Exercise 2 - ListView';

    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: title,
      home: Container(
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.black,
            width: 10.0,
          ),
        ),
        child: Scaffold(
          appBar: AppBar(
            title: const Text(title),
            backgroundColor: Colors.blue,
            titleTextStyle: const TextStyle(
              color: Colors.white,  // AppBar title text color
              fontWeight: FontWeight.bold,  // AppBar title text weight
              fontSize: 30,  // AppBar title text size
            ),
          ),
          body: ListView.builder(
            itemCount: 5,
            itemBuilder: (BuildContext context, int index) {
              // Calculate the item index in descending order
              int itemIndex = 4 - index;
              return ListTile(
                title: Text(
                  'Item $itemIndex',
                  style: const TextStyle(fontSize: 30),
                ),  // Increase title font size),
                subtitle: Text(
                  'This is the subtitle for item $itemIndex',
                  style: const TextStyle(fontSize: 25,
                  fontStyle: FontStyle.normal),
                ),
                leading: CircleAvatar(
                  child: Text(
                    '$itemIndex',
                    style: const TextStyle(fontSize: 30),
                    ),
                ),
                trailing: const Icon(Icons.favorite),
                onTap: () {
                  print('Tapped item $itemIndex');
                },
              );
            },
          ),
        ),
      ),
    );
  }
}
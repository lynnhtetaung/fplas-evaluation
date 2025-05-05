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
              color: Colors.white,
              fontWeight: FontWeight.bold,
              fontSize: 30,
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
                  style: const TextStyle(
                    fontSize: 30,
                    fontStyle: FontStyle.normal, // Remove italic style
                  ),
                ),
                subtitle: Text(
                  'This is the subtitle for item $itemIndex',
                  style: const TextStyle(
                    fontSize: 25,
                    fontStyle: FontStyle.normal, // Remove italic style
                  ),
                ),
                leading: CircleAvatar(
                  child: Text(
                    '$itemIndex',
                    style: const TextStyle(fontSize: 30),
                  ),
                ),
                trailing: const Icon(Icons.favorite), // Change icon to favorite
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

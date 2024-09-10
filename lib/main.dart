// import 'package:flutter/material.dart';

// void main() => runApp(const MyApp());

// class MyApp extends StatelessWidget {
//   const MyApp({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       debugShowCheckedModeBanner: false,
//       title: 'ListView Example',
//       home: Container(
//         decoration: BoxDecoration(
//           border: Border.all(
//             color: Colors.black,
//             width: 10.0,
//           ),
//         ),
//         child: Scaffold(
//           appBar: AppBar(
//             title: const Text('ListView Example'),
//           ),
//           body: ListView.builder(
//             itemCount: 5,
//             itemBuilder: (BuildContext context, int index) {
//               // Calculate the item index in descending order
//               int itemIndex = 4 - index;
//               return ListTile(
//                 title: Text('Item $itemIndex'),
//                 subtitle: Text('This is the subtitle for item $itemIndex'),
//                 leading: CircleAvatar(
//                   child: Text('$itemIndex'),
//                 ),
//                 // Change the trailing icon to a backward arrow
//                 trailing: const Icon(Icons.arrow_back),
//                 onTap: () {
//                   print('Tapped item $itemIndex');
//                 },
//               );
//             },
//           ),
//         ),
//       ),
//     );
//   }
// }

import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {

    const title = 'Exercise 2 - ListView Example';

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
            titleTextStyle: TextStyle(
              color: Colors.white, // AppBar title text color
              fontWeight: FontWeight.bold, // AppBar title text weight
              fontSize: 25, // AppBar title text size fontFamily: 'Raleway', // Use the Raleway font
              fontStyle: FontStyle.italic, // Set to italic
              fontFamily: 'Raleway', // Use the Raleway font
              fontStyle: FontStyle.italic, // Set to italic
            ),
          ),
          body: ListView.builder(
            itemCount: 5,
            itemBuilder: (BuildContext context, int index) {
              // Calculate the item index in descending order
              int itemIndex = index + 1;
              return ListTile(
                title: Text('Item $itemIndex'),
                subtitle: Text('This is the subtitle for item $itemIndex'),
                leading: CircleAvatar(
                  child: Text('$itemIndex'),
                ),
                // Change the trailing icon to a backward arrow
                trailing: const Icon(Icons.arrow_forward),
                onTap: () {
                  print('Tapped item $itemIndex');
                },
              );
            },
          ),
        ),
      ),
    );
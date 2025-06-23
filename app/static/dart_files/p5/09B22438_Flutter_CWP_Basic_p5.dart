import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Dropdown Example',
      home: DropdownExample(),
     );
  }
}

class DropdownExample extends StatefulWidget{
  @override
  _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample> {
  String selectedItem = 'Apple';
  final List<String> items = ['Apple','Banana','Orange','Grapes'];
  
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xFFFDF5FC),
      body: Center(
        child:Container(
          padding: EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          decoration: BoxDecoration(
            border: Border.all(color:Colors.redAccent),
            borderRadius: BorderRadius.circular(8),
            color: Color(0xFFFFF0F5),
           ),
           child: DropdownButton<String>(
             value:selectedItem,
             icon:Icon(Icons.arrow_drop_down),
             underline: SizeBox(),
             onChanged:(String? newValue){
               setState(() {
                 selectedItem = newValue!;                 
               });
             },
             items:items.map((String item) {
               return DropdownMenuItem<String>(
                 value: item,
                 child: Text(item),
                );
             }).toList(),
            ),
           ),
          ),
         );
  }
}
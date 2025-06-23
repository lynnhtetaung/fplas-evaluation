import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: DropdownExample(),
        );
    }
}

class DropdownExample extends StatefulWidget {
	@override
    _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample> {
	String _selectedValue = 'Apple';    
    List<String> _dropdownItems = ['Apple', 'Banana', 'Orange'];
    
    @override
    Widget build(BuildContext context) {
    	return Scaffold(
        	backgroundColor: Color(0xFFFAF0F8),
            body: Center(
            	child: Container(
            		padding: EdgeInsets.symmetric(horizontal: 12),
                	decoration: BoxDecoration(
                		border: Border.all(color: Colors.redAccent),
                        borderRadius: BorderRadius.circular(5),
                	),
               		child: DropdownButton<String>(
                		value: _selectedValue,
                    	underline: SizeBox(),
                    	items: _dropdownItems.map((String value) {
                    		return DropdownMenuItem<String>(
                        		value: value,
                            	child: Text(value),
                        	);
                    	}).toList(),
                    	onChanged: (newValue) {
                    		setState(() {
                        		_selectedValue = newValue!;
                    		});
                    	},
                	),
            	),
            ),
        );
    }
}
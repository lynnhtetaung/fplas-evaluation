import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	home: MyDropdown(),
        );
    }
}

class MyDropdown extends StatefulWidget {
	@override
    _MyDropdownState createState() => _MyDropdownState();
}

class _MyDropdownState extends State<MyDropdown> {
	String selectedValue = 'Apple';
    final List<String> items = ['Apple', 'Appl', 'App', 'Ap', 'A'];
    
    @override
    Widget build(BuildContext context) {
    	return Scaffold(
        	body: Center(
            	child: Container(
                	width: 200, height: 50,
                	padding: EdgeInsets.symmetric(horizontal: 20),
                    decoration: BoxDecoration(
                    	color: Colors.red[50],
                        border: Border.all(
                        	color: Colors.red,
                            width: 2,
                        ),
                        borderRadius: BorderRadius.circular(8),
                    ),
                	child: DropdownButton<String>(
                		value: selectedValue,
                        dropdownColor: Colors.red[50],
                        underline: SizedBox(),
                        isExpanded: true,
                    	items: items.map((String item) {
                    		return DropdownMenuItem<String>(
                        		value: item,
                            	child: Text(item),
                        	);
                    	}).toList(),
                    	onChanged: (String? newValue) {
                    		setState(() {
                        		selectedValue = newValue!;
                        	});
                    	},
                	),
            	),
        	),
        );
    }
}
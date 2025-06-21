import 'package:flutter/material.dart';

void main() {
	runApp(MyApp());
}

class MyApp extends StatelessWidget {
	@override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	title: 'Dropdown Example',
            home: DropdownScreen(),
        );
    }
}

class DropdownSample extends StatefulWidget {
	@override
    _DropdownSampleState createState() => _DropdownSampleState();
}

class _DropdownSampleState extends State<DropdownSample> {
	String selectedValue = 'りんご';
    
    final List<String> items = ['りんご', 'バナナ', 'オレンジ', 'ぶどう'];
	
    @override
    Widget build(BuildContext context) {
    	return Scaffold(
        	appBar: AppBar(title: Text('Dropdown Sample')),
            body: Center(
            	child: DropdownButton<string>(
                	value: selectedValue,
                    items: items.map((String value) {
                    	return DropdownMenuItem<String>(
                        	value: value,
                            child: Text(value),
                        );
                    }).toList(),
                    onChanged: (String? newValue) {
                    	setState(() {
                        	selectedValue = newValue!;
                        });
                    },
                ),
         ),
      );
    }
}
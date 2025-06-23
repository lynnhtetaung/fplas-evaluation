import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'Dropdown Demo',
            home: DropdownExample(),
        );
    }
}

class DropdownExample extends StatefulWidget{
	@override
    _DropdownExampleState createState() => _DropdownExampleState();
}

class _DropdownExampleState extends State<DropdownExample>{
	String _selectedValue = 'りんご';
    final List<String> _items = ['りんご','バナナ','ぶどう','みかん'];
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	appBar: AppBar(
            	title: Text('ドロップダウンメニュー'),
            ),
            body: Center(
            	child: DropdownButton<String>(
                	value: _selectedValue,
                    items: _items.map((String value){
                    	return DropdownMenuItem<String>(
                        	value: value,
                            child: Text(value),
                        );
                    }).toList(),
                    onChanged: (String? newValue){
                    	setState((){
                        	_selectedValue = newValue!;
                        });
                    },
                ),
            ),
        );
    }
}
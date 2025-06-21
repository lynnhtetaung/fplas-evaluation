import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	home: CheckboxExample(),
        );
    }
}

class CheckboxExample extends StatefulWidget{
	@override
    _CheckboxExampleState createState() => _CheckboxExampleState();
}

class _CheckboxExampleState extends State<CheckboxExample>{
	bool isChecked = true;
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	backgroundColor: Color(0xFFF9F0F7),
            body: Center(
            	child: Checkbox(
                	value: isChecked,
                    activeColor: Colors.blue,
                    onChanged: (bool? value){
                    	setState((){
                        	isChecked = value ?? false;
                        });
                    },
                ),
            ),
       );
    }
}
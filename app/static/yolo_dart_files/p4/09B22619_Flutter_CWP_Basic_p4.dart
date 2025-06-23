import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatelessWidget{
	@override
    Widget build(BuildContext context){
    	return MaterialApp(
        	title: 'Checkbox Demo',
            home: CheckboxExample(),
        );
    }
}

class CheckboxExample extends StatefulWidget{
	@override
    _CheckboxExampleState createState() => _CheckboxExampleState();
}

class _CheckboxExampleState extends State<CheckboxExample>{
	bool _isChecked = false;
    
    @override
    Widget build(BuildContext context){
    	return Scaffold(
        	
            body: Center(
            	child: Row(
                	mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                    	Checkbox(
                        	value: _isChecked,
                            onChanged: (bool? value){
                            	setState((){
                                	_isChecked = value ?? false;
                                });
                            },
                        ),

                    ],
                ),
            ),
        );
    }
}
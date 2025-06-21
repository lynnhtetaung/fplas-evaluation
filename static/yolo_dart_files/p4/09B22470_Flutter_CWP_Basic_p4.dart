import 'package:flutter/material.dart';

void main(){
	runApp(MyApp());
}

class MyApp extends StatefulWidget{
	@override
    State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp>{
	bool checked = true;
    
    @override
    Widget build(BuildContext context){
		return Center(
        	child: Checkbox(
            	value: checked,
                onChanged: (val) => setState(() => checked = val!),
            ),
        );
    }
}
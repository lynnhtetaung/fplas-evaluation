import 'package:flutter/material.dart';

void main () {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
	@override
	Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
    			body: Center(
                	child: SizedBox(
                	width: 250,
        				child: TextField(
                    		decoration: InputDecoration(
            				hintText: 'Enter name',
                        	hintStyle: TextStyle(color : Colors.green),
                            enabledBorder: OutlineInputBorder(
                            	borderSide: BorderSide(color: Colors.green),
                            ),
                        	),
            			),
            		),
            	),
        	),
    	);
    }
}
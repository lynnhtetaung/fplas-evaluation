import 'package:flutter/material.dart';

void main() {
	runApp(const MyApp());
}

class MyApp extends StatelessWidget {
	const MyApp({super.key});
    
    @override
    Widget build(BuildContext context) {
    	return MaterialApp(
        	home: Scaffold(
        		body: Center(
                	child: Container(
                    	width: 200,
                    	padding: const EdgeInsets.symmetric(horizontal: 25.0),
                        decoration: BoxDecoration(
                        		color: Colors.red.shade100,
                                borderRadius: BorderRadius.circular(15.0),
                                border: Border.all(color: Colors.red,width: 1.5),
                        	),
            			child: DropdownButton<String>(
                			value: 'Apple',
                			onChanged: (String? _) {},
                			items: <String>['Apple','Grape'].map<DropdownMenuItem<String>>((String value) {
                        		return DropdownMenuItem<String>(
                        			value: value,
                            		child: Text(value),
                        		);
                    		}).toList(),
                            underline: const SizedBox(),
                            isExpanded: true,
                    	),
                	),
            	),
        	),
    	);
    }
}
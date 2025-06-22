import 'package:flutter/material.dart';
import 'screens/table_overview.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Catering System',
      theme: ThemeData(primarySwatch: Colors.green),
      home: TableOverviewScreen(),
    );
  }
}

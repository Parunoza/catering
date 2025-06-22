import 'package:flutter/material.dart';

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

class TableOverviewScreen extends StatelessWidget {
  final int numberOfTables = 10; // Später konfigurierbar

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Tische')),
      body: GridView.builder(
        padding: EdgeInsets.all(16),
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2, // 2 Tische pro Zeile
          childAspectRatio: 1.5,
          mainAxisSpacing: 16,
          crossAxisSpacing: 16,
        ),
        itemCount: numberOfTables,
        itemBuilder: (context, index) {
          return ElevatedButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) => OrderScreen(tableNumber: index + 1),
                ),
              );
            },
            child: Text('Tisch ${index + 1}'),
          );
        },
      ),
    );
  }
}

class OrderScreen extends StatelessWidget {
  final int tableNumber;

  OrderScreen({required this.tableNumber});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bestellung - Tisch $tableNumber')),
      body: Center(
        child: Text('Hier kommt die Bestelloberfläche (Essen / Trinken)'),
      ),
    );
  }
}

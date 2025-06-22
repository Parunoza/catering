import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

/// Root widget for the application.
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

/// Overview screen displaying all tables in a grid.
class TableOverviewScreen extends StatelessWidget {
  final int numberOfTables =
      10; // Number of tables, can be made configurable later

  /// Sends a test message to the backend server from the overview screen.
  Future<void> sendTestMessage() async {
    final url = Uri.parse('http://10.0.1.3:8000/message'); // Local server IP
    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'text': 'Test von Uebersicht'}),
      );
      print('Server response: ${response.body}');
    } catch (e) {
      print('Error sending message: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Tables')),
      body: Column(
        children: [
          Expanded(
            child: GridView.builder(
              padding: EdgeInsets.all(16),
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
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
                        builder: (context) =>
                            OrderScreen(tableNumber: index + 1),
                      ),
                    );
                  },
                  child: Text('Table ${index + 1}'),
                );
              },
            ),
          ),
          // Button to test server communication
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: ElevatedButton(
              onPressed: sendTestMessage,
              child: Text('Send Test Message to Server'),
            ),
          ),
        ],
      ),
    );
  }
}

/// Screen shown when a table is selected, where orders will be placed.
class OrderScreen extends StatelessWidget {
  final int tableNumber;

  OrderScreen({required this.tableNumber});

  /// Sends a test message to the backend server from a specific table.
  Future<void> sendTestMessage() async {
    final url = Uri.parse('http://10.0.1.3:8000/message');
    try {
      final response = await http.post(
        url,
        headers: {'Content-Type': 'application/json'},
        body: json.encode({'text': 'Test from Table $tableNumber'}),
      );
      print('Server response: ${response.body}');
    } catch (e) {
      print('Error sending message: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Order - Table $tableNumber')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Ordering interface for food / drinks will be here.'),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: sendTestMessage,
              child: Text('Send Test Message to Server'),
            ),
          ],
        ),
      ),
    );
  }
}

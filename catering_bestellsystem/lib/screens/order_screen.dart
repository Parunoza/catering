import 'package:flutter/material.dart';
import '../services/api_service.dart';

class OrderScreen extends StatelessWidget {
  final int tableNumber;

  OrderScreen({required this.tableNumber});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bestellung - Tisch $tableNumber')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Hier kommt die Bestelloberfläche (Essen / Trinken)'),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () =>
                  ApiService.sendTestMessage('Test von Tisch $tableNumber'),
              child: Text('Test-Nachricht an Server'),
            ),
          ],
        ),
      ),
    );
  }
}

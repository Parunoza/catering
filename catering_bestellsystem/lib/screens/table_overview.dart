import 'package:flutter/material.dart';
import 'order_screen.dart';
import '../services/api_service.dart';

class TableOverviewScreen extends StatelessWidget {
  final int numberOfTables = 10;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Tische')),
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
                  child: Text('Tisch ${index + 1}'),
                );
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: ElevatedButton(
              onPressed: () => ApiService.sendTestMessage('Test von Übersicht'),
              child: Text('Testnachricht an Server'),
            ),
          ),
        ],
      ),
    );
  }
}

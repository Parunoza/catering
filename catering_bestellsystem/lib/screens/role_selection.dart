import 'package:flutter/material.dart';
import 'config.dart';
import 'main_screen_for_role.dart';

class RoleSelectionScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Rolle wählen')),
      body: ListView(
        children: UserRole.values.map((role) {
          final roleName = role.toString().split('.').last;
          return ListTile(
            title: Text(roleName),
            onTap: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (_) => MainScreenForRole(role: role),
                ),
              );
            },
          );
        }).toList(),
      ),
    );
  }
}

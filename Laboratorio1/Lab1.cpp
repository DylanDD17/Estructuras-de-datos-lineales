#include <iostream>
#include <string>
using namespace std;

int main() {
    const int N = 4;      // Numero de empleados
    const int SDN = 3;   // sueldo basico, deducciones, neto a pagar

    // Arreglo identificaciones
    int id[N] = {101, 102, 103, 104};
    
    // Arreglo nombres
    string nombres[N] = {"Ana", "Carlos", "Beatriz", "Diego"};
    
    // Arreglo bidimensional: sueldo basico, deducciones, neto a pagar
    float datos[N][SDN] = {
        {1200.0, 200.0, 0.0}, // Ana
        {1500.0, 250.0, 0.0}, // Carlos
        {1100.0, 150.0, 0.0}, // Beatriz
        {2000.0, 300.0, 0.0}  // Diego
    };
    
    // Calcular neto a pagar
    for (int i = 0; i < N; i++) 
    {
        datos[i][2] = datos[i][0] - datos[i][1];
    }
    
    // Mostrar arreglo de identificaciones
    cout << "Identificaciones:\n";
    for (int i = 0; i < N; i++) 
    {
        cout << id[i] << " ";
    }
    cout << "\n";
    
    // Mostrar arreglo de nombres
    cout << "\nNombres:\n";
    for (int i = 0; i < N; i++) 
    {
        cout << nombres[i] << " ";
    }
    cout << "\n";
    
    // Mostrar arreglo bidimensional con sueldos
    cout<<"\n";
    cout << "Sueldo basico\tDeducciones\tNeto a pagar\n";
    for (int i = 0; i < N; i++) 
    {
        cout
            << datos[i][1] << "\t\t" 
             << datos[i][2] << "\t\t" 
             << datos[i][3] << "\n";
    }
    
    // Buscar el id 
    int idBusqueda;
    bool encontrado = false;
    
    cout<<"\nEscriba el ID del empleado: ";
    cin>> idBusqueda;
    cout<<"\n";

    for (int i = 0; i < N; i++) 
    {
        if (id[i] == idBusqueda) 
        {
            cout << "\nEmpleado encontrado:\n";
            cout << "ID: " << id[i] << "\n";
            cout << "Nombre: " << nombres[i] << "\n";
            cout << "Sueldo basico: " << datos[i][0] << "\n";
            cout << "Deducciones: " << datos[i][1] << "\n";
            cout << "Neto a pagar: " << datos[i][2] << "\n";
            encontrado = true;
            break;
        }
    }

    if (!encontrado) 
    {
        cout << "\nEmpleado con ID " << idBusqueda << " no encontrado.\n";
    }

    return 0;
}
#include <iostream>
#include <string>
#include <list>
using namespace std;

int main() {
    const int N = 4; // Numero de empleados

    // Lista de identificaciones
    list<int> id = {101, 102, 103, 104};

    // Lista de nombres
    list<string> nombres = {"Ana", "Carlos", "Beatriz", "Diego"};

    // Lista de sueldos: cada empleado tiene (sueldo, deducciones, neto)
    list<list<float>> datos = {
        {1200.0, 200.0, 0.0}, // Ana
        {1500.0, 250.0, 0.0}, // Carlos
        {1100.0, 150.0, 0.0}, // Beatriz
        {2000.0, 300.0, 0.0}  // Diego
    };

    // Calcular neto a pagar
    for (auto& fila : datos) {
        auto it = fila.begin();
        float sueldo = *it;        // sueldo basico
        float deducciones = *(++it); 
        ++it;                      // apuntamos a neto
        *it = sueldo - deducciones;
    }

    // Mostrar lista de identificaciones
    cout << "Identificaciones:\n";
    for (auto x : id) {
        cout << x << " ";
    }
    cout << "\n";

    // Mostrar lista de nombres
    cout << "\nNombres:\n";
    for (auto x : nombres) {
        cout << x << " ";
    }
    cout << "\n";

    // Mostrar datos de sueldos
    cout << "\nSueldo basico\tDeducciones\tNeto a pagar\n";
    for (auto& fila : datos) {
        auto it = fila.begin();
        cout << *it << "\t\t"     // sueldo basico
             << *(++it) << "\t\t" // deducciones
             << *(++it) << "\n";  // neto
    }

    // Buscar empleado por ID
    int idBusqueda;
    cout << "\nEscriba el ID del empleado: ";
    cin >> idBusqueda;

    auto itId = id.begin();
    auto itNom = nombres.begin();
    auto itDat = datos.begin();

    bool encontrado = false;

    for (; itId != id.end(); ++itId, ++itNom, ++itDat) {
        if (*itId == idBusqueda) {
            cout << "\nEmpleado encontrado:\n";
            cout << "ID: " << *itId << "\n";
            cout << "Nombre: " << *itNom << "\n";

            auto it = itDat->begin();
            cout << "Sueldo basico: " << *it << "\n";
            cout << "Deducciones: " << *(++it) << "\n";
            cout << "Neto a pagar: " << *(++it) << "\n";

            encontrado = true;
            break;
        }
    }

    if (!encontrado) {
        cout << "\nEmpleado con ID " << idBusqueda << " no encontrado.\n";
    }

    return 0;
}

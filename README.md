# TecnoFix - Seguimiento de órdenes de reparación

## Descripción

Este repositorio contiene el módulo de seguimiento de órdenes de reparación
del sistema TecnoFix. El módulo permitirá crear órdenes, generar códigos
únicos, consultar información y controlar el estado de una reparación desde
la recepción del dispositivo hasta su entrega.

## Información académica

- Universidad: Universidad Estatal Amazónica
- Asignatura: Ingeniería de Software
- Autor: Juan Eduardo Vilchez Quintero
- Grupo: [Escribir el grupo registrado]
- Docente: Mgs. Hermes Darío Sánchez Bermeo

## Requerimientos atendidos

- RF-04: Crear una orden de reparación.
- RF-05: Generar un código único.
- RF-06: Registrar la falla, accesorios y datos de recepción.
- RF-07: Asignar un técnico.
- RF-09: Actualizar el estado de la orden.
- RF-10: Buscar órdenes.
- RF-11: Registrar la fecha y hora de los cambios.
- RF-13: Registrar la entrega del dispositivo.

## Tecnologías

- Python 3.12
- Flask
- Pytest
- GitHub Actions

## Flujo de trabajo

La rama `main` conservará la versión estable del proyecto.

Cada nueva función se desarrollará en una rama independiente. Por ejemplo:

- `feature/crear-orden`
- `feature/actualizar-estado`
- `feature/buscar-orden`
- `test/pruebas-ordenes`

Cuando un cambio esté terminado, se realizará un commit y se abrirá un
Pull Request hacia la rama `main`. La fusión se realizará cuando el pipeline
de GitHub Actions termine correctamente.

## Estados de una orden

- Recibido
- En diagnóstico
- En reparación
- Listo para retirar
- Entregado
- Cancelado

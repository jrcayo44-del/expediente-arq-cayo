<?php 
namespace Parcial1\Farmacia;
interface IRegistradorPedidos 
{ 
  public function registrarPedido( string $medicamento, int $cantidad ): void; 
} 
interface IAutorizadorControlados 
{ 
  public function autorizarVentaControlada( string $medicamento ): void; 
} 
interface IAjustadorPrecios 
{ 
  public function ajustarPrecio( string $medicamento, float $nuevoPrecio ): void; 
} 
interface ILectorControlados 
{ 
  public function verLibroDeControlados(): void; 
}

class Cajero implements IRegistradorPedidos 
{ 
  public function registrarPedido( string $medicamento, int $cantidad ): void { 
    echo "[CAJA] Pedido: {$cantidad} x {$medicamento}\n"; } 
}

class CalculadorDescuento 
{ 
  public function calcular( string $tipoCliente, float $total ): float { 
    switch ($tipoCliente) { 
      case "particular": 
        return 0; 
      case "asegurado": 
        return $total * 0.20; 
      case "convenio": 
        return $total * 0.10; 
      default: 
        return 0; 
    } 
  } 
}

class BaseDeDatosMySql 
{ 
  public function guardarPedido( 
    string $cliente, string $medicamento, int $cantidad, float $total 
  ): void 
  { echo "[MYSQL] INSERT INTO pedidos VALUES " . "('{$cliente}', '{$medicamento}', " . "{$cantidad}, {$total})\n"; } 
}

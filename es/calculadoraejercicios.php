<?php

$oper1 = $_GET['op1']

$oper2 = $_GET['op2']

$res = $_GET ['res']
/*$Switch ($Sol) {
	case suma
	    echo 'Es 8';
	break; */


/*switch ($i) {
    case 6:
        echo "i es igual a 6

";
    case 7:
        echo "i es igual a 7";
    case 8:
        echo "i es igual a 8";
} */


/*No funciona*/ 

function sumar (op1,  op2) {
	return op1 + op2
}

function restar (op1, op2) {
	return op1 - op2
}

function dividir (op1, op2) {
	return op1 - op2
}

function multiplicar (op1, op2) {
	return op1 * op2
}



switch ($res) {
	case 'Sumar':
	$res (op1, op2);
	break


echo "El resultado es $res";

?>

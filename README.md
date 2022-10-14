# Soporte de un Ingeniero para solucionar problema con ledger

Hola,

Soy usuario de sus dispositivos ledger desde hace mucho tiempo, y
les escribo este email para intentar solucionar un problema que tengo desde hace
algun tiempo con sus dispositivos, y necesitaria poder comunicarme con
alguno de sus ingenieros para solucionar el problema.

Tenia un dispositovo [LEDGER NANO] que compre alrededor de [FECHA DE COMPRA DEL
PRIMER DISPOSITIVO] el cual estuve utilizando durante un tiempo, y para el cual guarde mi
frase semilla.

Aproximadamente el dia [FECHA DE COMPRA DEL SEGUNDO DISPOSITIVO] decidi comprar un nuevo dispositivo
Ledger (modelo [AQUI MODELO DETALLADO DEL NUEVO LEDGER]), en el cual introduci
mi frase semilla y estuve usando sin problema durante algun tiempo. El dispositivo inicial
lo resetee, y ya no dispongo de el.

Alrededor del dia [FECHA DE ACTUALIZACION DEL SEGUNDO LEDGER] hubo una actualizacion
del firmware del ledger, y a partir de ese dia tuve problemas para acceder a mi direccion
de ethereum.

Entonces decidir comprar otro ledger, e introducir la frase semilla, sin embargo, seguia
sin generar mi direccion the ethereum original. Incluso haciendo reset del ledger que tenia,
e introduciendo mi frase semilla sigo sin poder acceder.

He recurrido a amigos que son profesionales del desarrollo de software y con conocimientos
de crytpo y blockchain, para intentar solucionar el problema.

Parece ser que a pesar de que esta estandarizada la forma de generar las direcciones y
claves privadas a partir de una frase semilla, diferentes dispositivos hardware pueden
utilizar diferentes "derivation paths" donde generar esas direcciones y claves privadas: (como
referencia, hay este articulo: https://medium.com/myetherwallet/hd-wallets-and-derivation-paths-explained-865a643c7bf2)

Mi sospecha es que debido a la actualizacion de firmware que tuvo el ledger, esos paths
han podido cambiar en algun momento, y al introducir la frase semilla en los nuevos
dispositivos ya no genera mi direccion y clave privada originales.

Asi pues, necesitaria saber todos los "derivation paths" que han podido ser usados
en los dispositivos ledger, para intentar recuperar el acceso a mi direccion. Asi como
cualquier otra pista que me pudiera dar alguno de sus ingenieros para saber si
puede haber algun otro problema que me estuviera impidiendo acceder a mi direccion.

Por otro lado, durante la investigacion / intento de solucionar mi problema, mi
amigo desarrollador preparo unos scripts para probar distintos "derivation paths",
a los cuales enlazo el codigo (para en caso que sus ingenieros quiran comprobar
que los procesos de prueba de los diferents "derivation paths" son correctos).

Me gustaria recalcar que:

1. Estoy seguro que mi frase semilla es correcta: nunca he apuntado otra frase semilla
    con la que me pudiera confundir, y ademas, esta comprobada porque pude usar
    un dispositivo ledger distinto en el pasado usando esa frase.
3. No he usado ningun password adicional para la generacion de las direcciones (soy
    consciente de hay la posibilidad de usar un password, pero no ha sido mi caso,
    yo solo he usado un pin para desbloquear el ledger cuando era necesario, pero
    no para la generacion de direcciones / claves privadas)


# Recover tree

run `./env.sh` to create the environment


## Ledger references

https://developers.ledger.com/docs/nano-app/psd-masterseed/

https://medium.com/myetherwallet/hd-wallets-and-derivation-paths-explained-865a643c7bf2



# TecnoAyuda

TecnoAyuda es un portal web de soporte técnico básico diseñado especialmente para estudiantes y usuarios cotidianos de tecnología. Su propósito es brindar soluciones sencillas, claras y explicadas paso a paso a los problemas más habituales en computadores y teléfonos celulares, sin tecnicismos innecesarios ni interfaces sobrecargadas.

---

## Desarrollador

- **Nombre:** Aaron Ramirez
- **Perfil:** Estudiante de enseñanza media.
- **Contexto:** Proyecto educativo desarrollado en Kodland.
- **Año de inicio:** 2026.

---

## Objetivo

> "Proyecto desarrollado con el objetivo de hacer que la tecnología sea más fácil de entender."

---

## Tecnologías Utilizadas

- **Python** (versión 3.x)
- **Flask** (microframework web)
- **HTML5** (marcado semántico y accesible)
- **CSS3** (diseño responsive puro, sin frameworks pesados ni dependencias externas)
- **JavaScript estándar** (para menú responsive móvil y checklist interactivo)

---

## Estructura del Proyecto

Archivos y carpetas reales que componen TecnoAyuda:

```text
TecnoAyuda/
├── app.py                      # Servidor web Flask, definición de rutas, motor de búsqueda y filtros
├── raw_kb.txt                  # Archivo de texto con las 301 guías de soporte redactadas
├── raw_kb_ampliado.txt         # Copia de la base de conocimiento ampliada (301 problemas)
├── raw_kb_backup_120.txt       # Respaldo de seguridad de la base original de 120 problemas
├── parse_kb.py                 # Script de compilación que convierte raw_kb.txt a problems.json
├── data/
│   └── problems.json           # Base de conocimiento principal estructurada en formato JSON (301 registros)
├── static/
│   ├── css/
│   │   └── style.css           # Hoja de estilos con paleta oscura, acento morado y responsive
│   ├── js/
│   │   └── main.js             # Lógica cliente para menú hamburguesa y checklist
│   ├── images/
│   │   ├── logo.png            # Logo oficial de TecnoAyuda en formato PNG
│   │   └── LEEME.txt           # Indicaciones sobre recursos gráficos
│   └── icons/
│       └── LEEME.txt           # Indicaciones sobre iconografía
└── templates/
    ├── base.html               # Plantilla maestra con navbar, menú móvil y footer estructurado
    ├── index.html              # Portada principal: hero centrado, buscador y accesos rápidos
    ├── pc.html                 # Soporte para PC con filtros de sistema (Windows, macOS, Linux)
    ├── celulares.html          # Soporte para Celulares con filtros de sistema (Android, iOS)
    ├── diagnostico.html        # Asistente de diagnóstico guiado en 3 pasos
    ├── buscar.html             # Resultados de búsqueda con sugerencias y estado vacío
    ├── problema.html           # Página individual de solución paso a paso y causas
    ├── herramientas.html       # Centro de herramientas de soporte técnico
    ├── mantenimiento.html      # Checklist de mantenimiento mensual interactivo
    ├── sobre.html              # Información sobre TecnoAyuda y datos de contacto oficiales
    ├── _tarjeta_problema.html  # Componente modular de tarjeta de problema
    └── 404.html                # Página amigable para rutas no encontradas
```

---

## Problemas Disponibles

Tras la ampliación y auditoría completa de los archivos del proyecto, se determinó que existen exactamente **301 problemas implementados y funcionales**.

### Distribución por Sistema Operativo / Plataforma

| Sistema | Cantidad de problemas |
| :--- | :---: |
| **Windows** | 73 |
| **Android** | 51 |
| **General** (aplica a múltiples dispositivos) | 47 |
| **iOS** | 47 |
| **macOS** | 45 |
| **Linux** | 38 |
| **TOTAL** | **301** |

### Distribución por Categoría (20 categorías en total)

| Categoría | Cantidad de problemas |
| :--- | :---: |
| **Aplicaciones** | 36 |
| **Internet** | 29 |
| **Almacenamiento** | 22 |
| **Pantalla** | 19 |
| **Sonido** | 19 |
| **Batería** | 17 |
| **Rendimiento** | 17 |
| **Sistema operativo** | 17 |
| **Archivos** | 16 |
| **Periféricos** | 16 |
| **Cuentas y sesiones** | 12 |
| **Impresoras** | 12 |
| **Seguridad** | 12 |
| **Actualizaciones** | 11 |
| **Bluetooth** | 11 |
| **Configuración** | 9 |
| **Cámara** | 8 |
| **Inicio del sistema** | 8 |
| **Dispositivos externos** | 5 |
| **Navegadores** | 5 |
| **TOTAL** | **301** |

---

## Problemas Faltantes

Actualmente existen **301 problemas implementados** de forma completa. Para llegar a 301 faltan **0 problemas** (catálogo ampliado y completado al 100%).

---

## Problemas Incompletos o Errores Detectados

- **Problemas incompletos:** **0**. Todos los 301 registros cuentan con título, descripción, causas comunes, solución secuencial paso a paso, nivel de dificultad, consejo de prevención y palabras clave.
- **Rutas rotas o problemas inexistentes:** **0**. Todas las rutas `/problema/<slug>` responden con código HTTP 200 OK y todos los enlaces de problemas relacionados hacen referencia a identificadores válidos dentro del rango 1..301.
- **Casos de títulos homónimos entre plataformas:** Existen 2 títulos que coinciden entre Android e iOS por tratarse de síntomas equivalentes en sistemas móviles distintos:
  - *"La pantalla táctil no responde bien"* (ID 71 para Android, ID 90 para iOS).
  - *"El micrófono no funciona en llamadas"* (ID 73 para Android, ID 92 para iOS).
  Ambos cuentan con slugs únicos (`la-pantalla-tactil-no-responde-bien` y `la-pantalla-tactil-no-responde-bien-2`), causas técnicas distintas y pasos específicos para su respectivo sistema operativo.

---

## Estado Detallado de los 301 Problemas

| ID | Problema | Sistema | Categoría | Estado |
| :-: | :--- | :--- | :--- | :--- |
| 1 | Windows tarda demasiado en iniciar | Windows | Rendimiento | Completo |
| 2 | El disco aparece al 100% en el Administrador de tareas | Windows | Rendimiento | Completo |
| 3 | Un programa no responde y se queda congelado | Windows | Aplicaciones | Completo |
| 4 | Windows Update no descarga actualizaciones | Windows | Actualizaciones | Completo |
| 5 | El PC no reconoce una memoria USB | Windows | Periféricos | Completo |
| 6 | El micrófono funciona pero las aplicaciones no lo detectan | Windows | Sonido | Completo |
| 7 | El Wi-Fi se desconecta constantemente | Windows | Internet | Completo |
| 8 | No hay sonido en los altavoces ni audífonos | Windows | Sonido | Completo |
| 9 | La pantalla se queda en negro al iniciar Windows | Windows | Inicio del sistema | Completo |
| 10 | Windows no encuentra redes Wi-Fi disponibles | Windows | Internet | Completo |
| 11 | El teclado deja de funcionar repentinamente | Windows | Periféricos | Completo |
| 12 | Los archivos se abren con el programa incorrecto | Windows | Archivos | Completo |
| 13 | El mouse se mueve demasiado rápido o lento | Windows | Periféricos | Completo |
| 14 | No se puede imprimir en la impresora | Windows | Impresoras | Completo |
| 15 | Windows Defender muestra advertencias constantemente | Windows | Seguridad | Completo |
| 16 | El PC se apaga solo sin advertencia | Windows | Rendimiento | Completo |
| 17 | No se puede conectar a Internet por cable Ethernet | Windows | Internet | Completo |
| 18 | Las ventanas se minimizan o maximizan solas | Windows | Sistema operativo | Completo |
| 19 | El almacenamiento se llena rápidamente | Windows | Almacenamiento | Completo |
| 20 | Windows no reconoce los audífonos Bluetooth | Windows | Bluetooth | Completo |
| 21 | Error "No hay espacio suficiente" al instalar programas | Windows | Almacenamiento | Completo |
| 22 | La cámara web no funciona en las aplicaciones | Windows | Cámara | Completo |
| 23 | Windows muestra pantalla azul (BSOD) frecuentemente | Windows | Sistema operativo | Completo |
| 24 | El touchpad no responde correctamente | Windows | Periféricos | Completo |
| 25 | Los íconos del escritorio desaparecieron | Windows | Sistema operativo | Completo |
| 26 | macOS ocupa demasiado espacio en "Datos del sistema" | macOS | Almacenamiento | Completo |
| 27 | Una aplicación no se abre o se cierra inmediatamente | macOS | Aplicaciones | Completo |
| 28 | El Mac está muy lento al abrir programas | macOS | Rendimiento | Completo |
| 29 | No se puede conectar a Wi-Fi en Mac | macOS | Internet | Completo |
| 30 | El trackpad no responde correctamente | macOS | Periféricos | Completo |
| 31 | macOS no reconoce dispositivos USB | macOS | Periféricos | Completo |
| 32 | No hay sonido en el Mac | macOS | Sonido | Completo |
| 33 | La batería del Mac se descarga muy rápido | macOS | Batería | Completo |
| 34 | Actualización de macOS falla o se queda pegada | macOS | Actualizaciones | Completo |
| 35 | El micrófono no funciona en aplicaciones | macOS | Sonido | Completo |
| 36 | Finder se congela o no responde | macOS | Sistema operativo | Completo |
| 37 | No se puede imprimir desde el Mac | macOS | Impresoras | Completo |
| 38 | La pantalla del Mac parpadea o tiene líneas | macOS | Pantalla | Completo |
| 39 | macOS no encuentra redes Bluetooth | macOS | Bluetooth | Completo |
| 40 | Los archivos no se pueden abrir | macOS | Archivos | Completo |
| 41 | Spotlight no encuentra archivos ni aplicaciones | macOS | Sistema operativo | Completo |
| 42 | El Mac se calienta demasiado | macOS | Rendimiento | Completo |
| 43 | Time Machine no realiza copias de seguridad | macOS | Almacenamiento | Completo |
| 44 | La cámara FaceTime no funciona | macOS | Cámara | Completo |
| 45 | macOS muestra el símbolo de prohibido al iniciar | macOS | Inicio del sistema | Completo |
| 46 | Ubuntu no reconoce la tarjeta Wi-Fi | Linux | Internet | Completo |
| 47 | No se pueden instalar programas desde la terminal | Linux | Aplicaciones | Completo |
| 48 | El sistema se congela después de actualizar | Linux | Actualizaciones | Completo |
| 49 | No hay sonido en Ubuntu | Linux | Sonido | Completo |
| 50 | El escritorio se ve con baja resolución | Linux | Pantalla | Completo |
| 51 | No se reconocen dispositivos USB | Linux | Periféricos | Completo |
| 52 | La terminal no responde a los comandos | Linux | Sistema operativo | Completo |
| 53 | No se puede conectar a Internet por cable | Linux | Internet | Completo |
| 54 | Los archivos no se pueden abrir con doble clic | Linux | Archivos | Completo |
| 55 | El sistema pide contraseña constantemente | Linux | Seguridad | Completo |
| 56 | No se puede imprimir en Linux | Linux | Impresoras | Completo |
| 57 | Ubuntu no detecta la tarjeta gráfica | Linux | Pantalla | Completo |
| 58 | El menú de aplicaciones no muestra todos los programas | Linux | Sistema operativo | Completo |
| 59 | No se puede montar una memoria USB | Linux | Periféricos | Completo |
| 60 | El sistema se vuelve lento con el tiempo | Linux | Rendimiento | Completo |
| 61 | Una aplicación de Android se cierra inmediatamente | Android | Aplicaciones | Completo |
| 62 | El celular se calienta demasiado | Android | Rendimiento | Completo |
| 63 | La batería dura muy poco | Android | Batería | Completo |
| 64 | El almacenamiento está lleno | Android | Almacenamiento | Completo |
| 65 | El Wi-Fi se conecta pero no tiene Internet | Android | Internet | Completo |
| 66 | Bluetooth no encuentra mis audífonos | Android | Bluetooth | Completo |
| 67 | La cámara toma fotos borrosas | Android | Cámara | Completo |
| 68 | El sonido del celular es muy bajo | Android | Sonido | Completo |
| 69 | No se pueden descargar aplicaciones de Play Store | Android | Aplicaciones | Completo |
| 70 | El celular no carga la batería | Android | Batería | Completo |
| 71 | La pantalla táctil no responde bien | Android | Pantalla | Completo |
| 72 | No llegan las notificaciones de WhatsApp | Android | Aplicaciones | Completo |
| 73 | El micrófono no funciona en llamadas | Android | Sonido | Completo |
| 74 | Android se actualiza muy lento | Android | Actualizaciones | Completo |
| 75 | No se puede conectar a Wi-Fi | Android | Internet | Completo |
| 76 | Los archivos descargados no aparecen | Android | Archivos | Completo |
| 77 | El celular no reconoce la tarjeta SD | Android | Almacenamiento | Completo |
| 78 | Las aplicaciones consumen demasiada batería | Android | Batería | Completo |
| 79 | No se puede hacer llamadas | Android | Internet | Completo |
| 80 | El GPS no funciona correctamente | Android | Aplicaciones | Completo |
| 81 | El iPhone se queda sin espacio aunque borre fotos | iOS | Almacenamiento | Completo |
| 82 | La batería del iPhone dura muy poco | iOS | Batería | Completo |
| 83 | Una aplicación se cierra sola en iPhone | iOS | Aplicaciones | Completo |
| 84 | El iPhone no se conecta a Wi-Fi | iOS | Internet | Completo |
| 85 | Bluetooth no conecta con audífonos | iOS | Bluetooth | Completo |
| 86 | La cámara del iPhone toma fotos oscuras | iOS | Cámara | Completo |
| 87 | El sonido del iPhone es muy bajo | iOS | Sonido | Completo |
| 88 | No se pueden descargar aplicaciones del App Store | iOS | Aplicaciones | Completo |
| 89 | El iPhone no carga la batería | iOS | Batería | Completo |
| 90 | La pantalla táctil no responde bien | iOS | Pantalla | Completo |
| 91 | No llegan las notificaciones en iPhone | iOS | Aplicaciones | Completo |
| 92 | El micrófono no funciona en llamadas | iOS | Sonido | Completo |
| 93 | iOS se actualiza muy lento | iOS | Actualizaciones | Completo |
| 94 | El iPhone no encuentra redes Wi-Fi | iOS | Internet | Completo |
| 95 | Los archivos no se pueden abrir en iPhone | iOS | Archivos | Completo |
| 96 | El iPhone se calienta demasiado | iOS | Rendimiento | Completo |
| 97 | FaceTime no funciona correctamente | iOS | Aplicaciones | Completo |
| 98 | El iPhone no reconoce los audífonos | iOS | Periféricos | Completo |
| 99 | AirDrop no encuentra dispositivos cercanos | iOS | Bluetooth | Completo |
| 100 | Siri no responde a los comandos | iOS | Aplicaciones | Completo |
| 101 | El cargador no carga el dispositivo | General | Batería | Completo |
| 102 | Los audífonos no suenan bien | General | Sonido | Completo |
| 103 | El dispositivo no reconoce la memoria USB | General | Periféricos | Completo |
| 104 | La pantalla se ve con colores extraños | General | Pantalla | Completo |
| 105 | El teclado no escribe las letras correctas | General | Periféricos | Completo |
| 106 | El mouse no se mueve correctamente | General | Periféricos | Completo |
| 107 | La impresora no imprime | General | Impresoras | Completo |
| 108 | El Wi-Fi es muy lento | General | Internet | Completo |
| 109 | El dispositivo se apaga solo | General | Batería | Completo |
| 110 | Las aplicaciones se cierran solas | General | Aplicaciones | Completo |
| 111 | Windows no detecta la impresora | Windows | Impresoras | Completo |
| 112 | El PC hace demasiado ruido | Windows | Rendimiento | Completo |
| 113 | Windows Update se queda pegado | Windows | Actualizaciones | Completo |
| 114 | El PC no entra en modo suspensión | Windows | Sistema operativo | Completo |
| 115 | Los archivos temporales ocupan mucho espacio | Windows | Almacenamiento | Completo |
| 116 | macOS no abre aplicaciones de desarrolladores no identificados | macOS | Seguridad | Completo |
| 117 | El Mac no despierta del modo suspensión | macOS | Sistema operativo | Completo |
| 118 | Ubuntu muestra error de espacio en disco | Linux | Almacenamiento | Completo |
| 119 | Android muestra "Almacenamiento en ejecución" | Android | Almacenamiento | Completo |
| 120 | iOS muestra "Almacenamiento casi lleno" | iOS | Almacenamiento | Completo |
| 121 | El menú Inicio o la barra de tareas no responde | Windows | Sistema operativo | Completo |
| 122 | La búsqueda de Windows no encuentra archivos o programas | Windows | Sistema operativo | Completo |
| 123 | Windows no detecta el segundo monitor | Windows | Pantalla | Completo |
| 124 | Los textos y programas se ven borrosos o demasiado grandes en Windows | Windows | Pantalla | Completo |
| 125 | La herramienta de recortes o las capturas de pantalla no funcionan | Windows | Aplicaciones | Completo |
| 126 | Copiar y pegar no funciona en Windows | Windows | Aplicaciones | Completo |
| 127 | Windows se conecta al Wi-Fi pero dice "Sin Internet" | Windows | Internet | Completo |
| 128 | Las páginas no cargan por un proxy o VPN mal configurado | Windows | Internet | Completo |
| 129 | La fecha y la hora de Windows están incorrectas | Windows | Configuración | Completo |
| 130 | OneDrive no sincroniza mis archivos | Windows | Archivos | Completo |
| 131 | No puedo iniciar sesión en Windows con mi cuenta de Microsoft | Windows | Cuentas y sesiones | Completo |
| 132 | Windows Hello, el PIN o la huella dejan de funcionar | Windows | Cuentas y sesiones | Completo |
| 133 | Windows pide una clave de recuperación de BitLocker | Windows | Seguridad | Completo |
| 134 | Windows muestra "Activar Windows" en la esquina de la pantalla | Windows | Sistema operativo | Completo |
| 135 | Microsoft Store no abre o no descarga aplicaciones | Windows | Aplicaciones | Completo |
| 136 | Windows Update muestra un código de error y no instala | Windows | Actualizaciones | Completo |
| 137 | El mouse o teclado Bluetooth se desconecta o no responde | Windows | Bluetooth | Completo |
| 138 | No sale sonido por HDMI hacia el televisor o monitor | Windows | Sonido | Completo |
| 139 | Un disco duro o SSD nuevo no aparece en "Este equipo" | Windows | Almacenamiento | Completo |
| 140 | El disco duro externo no es reconocido o suena pero no abre | Windows | Dispositivos externos | Completo |
| 141 | No puedo expulsar la memoria USB: "El dispositivo está en uso" | Windows | Dispositivos externos | Completo |
| 142 | La memoria USB está protegida contra escritura | Windows | Archivos | Completo |
| 143 | No puedo borrar, mover o renombrar un archivo o carpeta | Windows | Archivos | Completo |
| 144 | No se puede descomprimir un archivo ZIP o RAR | Windows | Archivos | Completo |
| 145 | No puedo instalar o ver una fuente (tipografía) en Windows | Windows | Aplicaciones | Completo |
| 146 | El teclado escribe símbolos raros o cambia de idioma solo | Windows | Configuración | Completo |
| 147 | No puedo cambiar el brillo de la pantalla en Windows | Windows | Pantalla | Completo |
| 148 | La batería del notebook con Windows dura muy poco | Windows | Batería | Completo |
| 149 | El escáner de la impresora multifuncional no funciona | Windows | Impresoras | Completo |
| 150 | La impresora aparece "Sin conexión" aunque está encendida | Windows | Impresoras | Completo |
| 151 | Un documento se queda atascado en la cola de impresión | Windows | Impresoras | Completo |
| 152 | El Mac no enciende o la pantalla se queda en negro | macOS | Inicio del sistema | Completo |
| 153 | El MacBook no carga o el cargador no es reconocido | macOS | Batería | Completo |
| 154 | El Mac se conecta al Wi-Fi pero Internet va lento | macOS | Internet | Completo |
| 155 | El Magic Mouse, Magic Keyboard u otro accesorio Bluetooth no conecta en Mac | macOS | Bluetooth | Completo |
| 156 | El Mac no detecta el monitor externo o el proyector | macOS | Pantalla | Completo |
| 157 | El Dock, la barra de menú o las ventanas se comportan raro en Mac | macOS | Sistema operativo | Completo |
| 158 | Safari está lento o se cierra en el Mac | macOS | Aplicaciones | Completo |
| 159 | Olvidé la contraseña de inicio de sesión del Mac | macOS | Cuentas y sesiones | Completo |
| 160 | iCloud no sincroniza archivos, fotos o contactos en el Mac | macOS | Cuentas y sesiones | Completo |
| 161 | La App Store del Mac no descarga ni actualiza aplicaciones | macOS | Aplicaciones | Completo |
| 162 | Mis archivos del Escritorio y Documentos desaparecieron en el Mac | macOS | Archivos | Completo |
| 163 | Aparece la rueda de colores (bola de playa) y el Mac se congela | macOS | Rendimiento | Completo |
| 164 | El sonido por Bluetooth se corta o suena con retraso en el Mac | macOS | Sonido | Completo |
| 165 | Una aplicación no puede usar la cámara, micrófono o archivos en Mac | macOS | Seguridad | Completo |
| 166 | El Mac se queda en la manzana con barra de carga o reinicia en bucle | macOS | Inicio del sistema | Completo |
| 167 | El Mac sigue lleno aunque borré archivos | macOS | Almacenamiento | Completo |
| 168 | El Mac no recuerda la contraseña del Wi-Fi o pide la clave siempre | macOS | Internet | Completo |
| 169 | macOS no tiene espacio para descargar la actualización | macOS | Actualizaciones | Completo |
| 170 | La cámara del Mac no funciona en Zoom, Meet o Teams | macOS | Cámara | Completo |
| 171 | AirPlay o duplicar pantalla en la TV no aparece desde el Mac | macOS | Pantalla | Completo |
| 172 | Ubuntu dice "No se pudo obtener el bloqueo" al instalar programas | Linux | Aplicaciones | Completo |
| 173 | Ubuntu no puede actualizar porque la partición /boot está llena | Linux | Almacenamiento | Completo |
| 174 | Ubuntu muestra errores de repositorio o clave GPG al actualizar | Linux | Actualizaciones | Completo |
| 175 | Bluetooth no funciona o no aparece en Ubuntu | Linux | Bluetooth | Completo |
| 176 | El Wi-Fi en Ubuntu es lento o se desconecta | Linux | Internet | Completo |
| 177 | Ubuntu no encuentra la impresora de red | Linux | Impresoras | Completo |
| 178 | Ubuntu muestra pantalla negra después de instalar el controlador NVIDIA | Linux | Pantalla | Completo |
| 179 | El PC con doble arranque no muestra Ubuntu o Windows al iniciar | Linux | Inicio del sistema | Completo |
| 180 | La hora está incorrecta al usar Windows y Ubuntu en el mismo PC | Linux | Configuración | Completo |
| 181 | Las aplicaciones Snap tardan mucho en abrir o no se actualizan | Linux | Aplicaciones | Completo |
| 182 | La terminal no muestra nada al escribir la contraseña de sudo | Linux | Seguridad | Completo |
| 183 | El PC no arranca desde el pendrive de instalación de Ubuntu | Linux | Dispositivos externos | Completo |
| 184 | El audio por Bluetooth no funciona en Ubuntu | Linux | Sonido | Completo |
| 185 | Ubuntu dice "Permiso denegado" al abrir o guardar un archivo | Linux | Archivos | Completo |
| 186 | Los textos e íconos se ven demasiado pequeños o grandes en Ubuntu | Linux | Pantalla | Completo |
| 187 | El escritorio de Ubuntu se queda congelado pero el mouse se mueve | Linux | Sistema operativo | Completo |
| 188 | Ubuntu pide la contraseña del Wi-Fi cada vez que enciendo el equipo | Linux | Internet | Completo |
| 189 | Un archivo .deb, .AppImage o .tar.gz no se abre ni se instala en Ubuntu | Linux | Aplicaciones | Completo |
| 190 | Ubuntu se vuelve extremadamente lento cuando se llena la memoria | Linux | Rendimiento | Completo |
| 191 | Un disco de Windows se monta como solo lectura en Ubuntu | Linux | Almacenamiento | Completo |
| 192 | El celular Android no enciende o se queda en el logo | Android | Inicio del sistema | Completo |
| 193 | El celular Android se reinicia o se apaga solo | Android | Rendimiento | Completo |
| 194 | No me entran llamadas o los contactos no aparecen al llamar | Android | Aplicaciones | Completo |
| 195 | El celular no tiene señal ni datos móviles | Android | Internet | Completo |
| 196 | La zona Wi-Fi (compartir Internet) no funciona en Android | Android | Internet | Completo |
| 197 | El celular Android está muy lento o se traba | Android | Rendimiento | Completo |
| 198 | La pantalla del celular hace toques solos o tiene manchas | Android | Pantalla | Completo |
| 199 | El brillo de la pantalla cambia solo o se ve muy oscuro | Android | Pantalla | Completo |
| 200 | Android pide iniciar sesión en la cuenta de Google o no la sincroniza | Android | Cuentas y sesiones | Completo |
| 201 | Google Play muestra error al pagar o descargar una app | Android | Aplicaciones | Completo |
| 202 | La cámara del celular tarda en abrir o falla al enfocar | Android | Cámara | Completo |
| 203 | Las fotos de Android no se respaldan en Google Fotos | Android | Archivos | Completo |
| 204 | El PC no ve los archivos del celular Android al conectarlo por USB | Android | Dispositivos externos | Completo |
| 205 | WhatsApp no descarga fotos, audios o archivos | Android | Aplicaciones | Completo |
| 206 | La copia de seguridad de WhatsApp falla en Android | Android | Aplicaciones | Completo |
| 207 | El celular Android no se conecta al auto por Bluetooth | Android | Bluetooth | Completo |
| 208 | El celular Android carga muy lento | Android | Batería | Completo |
| 209 | El porcentaje de batería salta de golpe o se apaga con 20-30% | Android | Batería | Completo |
| 210 | El celular no se conecta al Wi-Fi del colegio o de la universidad | Android | Internet | Completo |
| 211 | En llamadas se escucha eco o la otra persona no me escucha bien | Android | Sonido | Completo |
| 212 | El celular no suena ni vibra con notificaciones | Android | Configuración | Completo |
| 213 | La alarma del celular no suena a la hora programada | Android | Aplicaciones | Completo |
| 214 | Una aplicación ocupa demasiado espacio en Android | Android | Almacenamiento | Completo |
| 215 | Google Maps no encuentra mi ubicación exacta | Android | Configuración | Completo |
| 216 | Los datos móviles se gastan demasiado rápido | Android | Internet | Completo |
| 217 | El iPhone no enciende o se queda en la manzana | iOS | Inicio del sistema | Completo |
| 218 | El iPhone se reinicia o se cierra solo | iOS | Rendimiento | Completo |
| 219 | Face ID o Touch ID no funcionan | iOS | Cuentas y sesiones | Completo |
| 220 | Olvidé el código de desbloqueo del iPhone o aparece "iPhone no disponible" | iOS | Cuentas y sesiones | Completo |
| 221 | iCloud está lleno y el iPhone no hace copias de seguridad | iOS | Almacenamiento | Completo |
| 222 | Las fotos del iPhone no se sincronizan con iCloud | iOS | Archivos | Completo |
| 223 | iOS dice que no hay suficiente espacio para actualizar | iOS | Actualizaciones | Completo |
| 224 | El iPhone dice "Contraseña incorrecta" al conectar al Wi-Fi | iOS | Internet | Completo |
| 225 | El iPhone no tiene datos móviles o no recibe señal | iOS | Internet | Completo |
| 226 | Punto de acceso personal del iPhone no funciona | iOS | Internet | Completo |
| 227 | El iPhone está lento o se traba | iOS | Rendimiento | Completo |
| 228 | La pantalla del iPhone parpadea, tiene líneas o se pone verde | iOS | Pantalla | Completo |
| 229 | iMessage o SMS no se envían desde el iPhone | iOS | Aplicaciones | Completo |
| 230 | Las aplicaciones del iPhone no se actualizan | iOS | Aplicaciones | Completo |
| 231 | El iPhone dice "Servicio de batería" o la salud de la batería es baja | iOS | Batería | Completo |
| 232 | El iPhone muestra "Accesorio no compatible" al cargar | iOS | Batería | Completo |
| 233 | Los AirPods no se conectan o solo suena un lado | iOS | Bluetooth | Completo |
| 234 | El micrófono del iPhone no funciona en Zoom, Meet o videollamadas | iOS | Sonido | Completo |
| 235 | La cámara del iPhone no enfoca o muestra pantalla negra | iOS | Cámara | Completo |
| 236 | Una app ocupa mucho espacio en iPhone (Datos y documentos) | iOS | Almacenamiento | Completo |
| 237 | El Apple ID está bloqueado o pide verificación constantemente | iOS | Cuentas y sesiones | Completo |
| 238 | El altavoz del iPhone suena apagado o con distorsión | iOS | Sonido | Completo |
| 239 | El teclado, el dictado o las sugerencias no funcionan en el iPhone | iOS | Configuración | Completo |
| 240 | El navegador no carga páginas aunque hay Wi-Fi | General | Navegadores | Completo |
| 241 | El navegador está lento o consume mucha memoria | General | Navegadores | Completo |
| 242 | El navegador muestra "Su conexión no es privada" o error de certificado | General | Navegadores | Completo |
| 243 | Aparecen ventanas emergentes, publicidad o páginas raras en el navegador | General | Seguridad | Completo |
| 244 | El navegador no guarda las contraseñas o no completa los formularios | General | Cuentas y sesiones | Completo |
| 245 | El navegador bloquea o no completa las descargas | General | Navegadores | Completo |
| 246 | Los videos de YouTube se cortan, se ven pixelados o no cargan | General | Navegadores | Completo |
| 247 | En clases virtuales no se escucha o no se ve a nadie | General | Aplicaciones | Completo |
| 248 | Word, Excel o PowerPoint no abren un archivo o piden activar | General | Aplicaciones | Completo |
| 249 | Un archivo PDF no abre o se ve en blanco | General | Archivos | Completo |
| 250 | Recibí un correo o mensaje sospechoso pidiendo datos o contraseñas | General | Seguridad | Completo |
| 251 | Creo que alguien entró a mi cuenta (redes sociales, correo o juegos) | General | Seguridad | Completo |
| 252 | Creo que mi computador o celular tiene un virus | General | Seguridad | Completo |
| 253 | El Internet de la casa se cae o va intermitente | General | Internet | Completo |
| 254 | La señal Wi-Fi es débil en ciertas habitaciones | General | Internet | Completo |
| 255 | La pantalla del monitor parpadea o se apaga por momentos | General | Pantalla | Completo |
| 256 | Aparece una mancha, línea o píxel que no cambia en la pantalla | General | Pantalla | Completo |
| 257 | Algunas teclas del notebook no funcionan o se repiten | General | Periféricos | Completo |
| 258 | El touchpad se desactiva o hace clic solo | General | Periféricos | Completo |
| 259 | El notebook se levanta, no cierra bien o la base está abultada | General | Batería | Completo |
| 260 | El ventilador del notebook hace ruido o se calienta mucho | General | Rendimiento | Completo |
| 261 | Los audífonos con micrófono no se escuchan o no capturan la voz | General | Sonido | Completo |
| 262 | Los parlantes hacen ruido, zumbido o estática | General | Sonido | Completo |
| 263 | La tarjeta SD o microSD muestra error o está vacía | General | Almacenamiento | Completo |
| 264 | No sé qué ocupa espacio en mi computador | General | Almacenamiento | Completo |
| 265 | ¿Cómo hago una copia de seguridad básica de mis archivos? | General | Archivos | Completo |
| 266 | No puedo guardar o abrir un archivo por caracteres o nombre muy largo | General | Archivos | Completo |
| 267 | No puedo copiar un archivo grande a mi pendrive | General | Almacenamiento | Completo |
| 268 | El código de verificación en dos pasos no funciona | General | Cuentas y sesiones | Completo |
| 269 | El cable USB-C carga lento o no transmite datos ni video | General | Batería | Completo |
| 270 | No puedo conectar la impresora al Wi-Fi | General | Impresoras | Completo |
| 271 | La impresora tiene atasco de papel o toma varias hojas | General | Impresoras | Completo |
| 272 | La impresora imprime con rayas, manchas o colores incorrectos | General | Impresoras | Completo |
| 273 | Un programa o juego dice que falta un archivo DLL (VCRUNTIME140.dll, MSVCP140.dll) | Windows | Aplicaciones | Completo |
| 274 | Windows bloquea un instalador con "Windows protegió su PC" | Windows | Seguridad | Completo |
| 275 | El Administrador de dispositivos muestra un triángulo amarillo en un dispositivo | Windows | Periféricos | Completo |
| 276 | Quiero iniciar Windows en modo seguro para solucionar un problema | Windows | Inicio del sistema | Completo |
| 277 | Quiero volver Windows a un estado anterior después de que algo falló | Windows | Sistema operativo | Completo |
| 278 | Windows emite pitidos o pide activar "Teclas especiales" al presionar Shift varias veces | Windows | Configuración | Completo |
| 279 | No aparecen las notificaciones en Windows | Windows | Configuración | Completo |
| 280 | Los juegos van lentos o con pocos cuadros por segundo en el PC | Windows | Rendimiento | Completo |
| 281 | El modo avión de Windows queda activado y no deja conectarse | Windows | Internet | Completo |
| 282 | Una aplicación específica no tiene sonido pero el resto sí | Windows | Sonido | Completo |
| 283 | El cursor del mouse desaparece o no se ve al escribir | Windows | Periféricos | Completo |
| 284 | Quiero restablecer Windows pero no quiero perder mis archivos | Windows | Sistema operativo | Completo |
| 285 | Una aplicación del Mac no responde y no se puede cerrar | macOS | Aplicaciones | Completo |
| 286 | El Bluetooth del Mac aparece desactivado o no se puede activar | macOS | Bluetooth | Completo |
| 287 | No funcionan las capturas de pantalla en el Mac | macOS | Aplicaciones | Completo |
| 288 | Ubuntu no despierta de la suspensión o la pantalla queda negra | Linux | Sistema operativo | Completo |
| 289 | La terminal dice "command not found" (comando no encontrado) | Linux | Aplicaciones | Completo |
| 290 | Google Play Protect bloquea una aplicación o muestra una advertencia | Android | Seguridad | Completo |
| 291 | Android Auto no conecta con el auto | Android | Dispositivos externos | Completo |
| 292 | El teclado de Android no aparece, se traba o escribe palabras incorrectas | Android | Aplicaciones | Completo |
| 293 | No veo el contenido de las notificaciones en la pantalla de bloqueo | Android | Configuración | Completo |
| 294 | Las aplicaciones de Android no se actualizan solas | Android | Actualizaciones | Completo |
| 295 | La grabación de pantalla del iPhone no tiene sonido o no se guarda | iOS | Cámara | Completo |
| 296 | La pantalla del iPhone no gira o se queda bloqueada en vertical | iOS | Pantalla | Completo |
| 297 | El correo del iPhone no se actualiza o no recibe mensajes | iOS | Cuentas y sesiones | Completo |
| 298 | No me llegan correos importantes o caen en spam | General | Cuentas y sesiones | Completo |
| 299 | Google Drive o Gmail dicen que el almacenamiento está lleno | General | Almacenamiento | Completo |
| 300 | El notebook dice "Enchufado, no se está cargando" | General | Batería | Completo |
| 301 | No recuerdo la contraseña del Wi-Fi de mi casa | General | Internet | Completo |

---

## Rutas Principales del Proyecto

- `/`: Portada principal con buscador, accesos rápidos, problemas frecuentes y acceso a herramientas.
- `/buscar`: Buscador de problemas con filtrado por palabras clave (`?q=`).
- `/pc`: Soporte técnico para computadores de escritorio y notebooks (filtros por `?sistema=` y `?categoria=`).
- `/celulares`: Soporte técnico para teléfonos inteligentes (filtros por `?sistema=` y `?categoria=`).
- `/diagnostico`: Asistente por etapas para diagnosticar una falla según dispositivo y síntomas.
- `/problema/<slug>`: Ficha individual detallada con causas, pasos de solución, consejos y temas relacionados.
- `/herramientas`: Panel de utilidades de asistencia y mantenimiento.
- `/mantenimiento`: Checklist mensual interactivo para estudiantes y usuarios.
- `/sobre`: Información sobre el proyecto TecnoAyuda, objetivos y contacto.
- Error 404: Manejador amigable de páginas no encontradas.

---

## Próximas Mejoras Sugeridas

1. **Capturas ilustrativas:** Añadir imágenes y diagramas paso a paso en las soluciones más consultadas.
2. **Exportación de Checklist:** Permitir descargar o imprimir el checklist de mantenimiento preventivo mensual.
3. **Modo fuera de línea (PWA):** Añadir un Service Worker para permitir consultar soluciones guardadas sin conexión activa a internet.
4. **Historial de consultas recientes:** Permitir al usuario volver a revisar las últimas soluciones consultadas en su navegador.

---

## Información de Contacto

- **Correo electrónico:** [aaronramirezveliz874@gmail.com](mailto:aaronramirezveliz874@gmail.com)
- **Desarrollador:** Aaron Ramirez
- **Sitio:** TecnoAyuda (2026)

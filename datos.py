# =================================================================
# BASE DE CONOCIMIENTO DEL AGENTE TAOISTA - VERSIÓN EXTENDIDA
# =================================================================

# 1. DATOS DE ENTRENAMIENTO
# -----------------------------------------------------------------
# Aquí es donde ocurre la magia. Cuantos más ejemplos, más listo se vuelve.
# -----------------------------------------------------------------
datos = [
    # --- LOTE 1: MIX GENERAL (YA INCLUIDO) ---
    # TRISTEZA
    ("Me siento muy triste y sin esperanza", "tristeza"),
    ("Siento que nada tiene sentido, estoy vacío", "tristeza"),
    ("Siento un vacío enorme que no puedo llenar con nada", "tristeza"),
    ("Hoy me levanté sin ganas de existir", "tristeza"),
    ("Todo lo que toco parece romperse", "tristeza"),
    ("Extraño tiempos mejores y me duele el pecho", "tristeza"),
    ("Nadie me entiende, estoy completamente solo", "tristeza"),
    ("La melancolía me atrapó esta tarde", "tristeza"),
    ("He llorado sin razón aparente", "tristeza"),
    ("Siento que estoy sobrando en este mundo", "tristeza"),
    ("Mi corazón está roto en mil pedazos", "tristeza"),
    ("No encuentro consuelo en ninguna parte", "tristeza"),

    # ANSIEDAD
    ("Tengo mucha ansiedad y miedo por el futuro", "ansiedad"),
    ("Estoy inquieto, no puedo dejar de pensar", "ansiedad"),
    ("Tengo un nudo en el estómago que no se quita", "ansiedad"),
    ("Siento que algo malo va a pasar pronto", "ansiedad"),
    ("No puedo dejar de mover la pierna, estoy muy nervioso", "ansiedad"),
    ("Me estoy ahogando en mis propios pensamientos", "ansiedad"),
    ("El futuro me aterra demasiado", "ansiedad"),
    ("Siento taquicardia y me falta el aire", "ansiedad"),
    ("¿Y si fallo? ¿Y si todos se burlan?", "ansiedad"),
    ("Mi mente va a mil por hora y no frena", "ansiedad"),
    ("Necesito controlar todo o me desespero", "ansiedad"),
    ("Siento que pierdo el control de mi vida", "ansiedad"),

    # IRA / FRUSTRACIÓN
    ("Tengo mucha ira, estoy enojado con todos", "ira"),
    ("Odio que las cosas no salgan como quiero", "ira"),
    ("Estoy harto de que me digan qué hacer", "ira"),
    ("Quiero gritar hasta quedarme sin voz", "ira"),
    ("Me revienta que la gente sea tan hipócrita", "ira"),
    ("Todo me sale mal, maldita sea", "ira"),
    ("No soporto ver a nadie hoy", "ira"),
    ("Me hierve la sangre cuando veo injusticias", "ira"),
    ("Tengo ganas de golpear la pared", "ira"),
    ("Estoy furioso conmigo mismo por ser así", "ira"),
    ("Odio sentirme tan impotente", "ira"),
    ("La estupidez humana me tiene cansado", "ira"),

    # CALMA / PAZ
    ("Estoy en paz, todo fluye bien", "calma"),
    ("Me siento agradecido con la vida", "calma"),
    ("Hoy el aire se siente más ligero", "calma"),
    ("Disfruto del silencio de mi habitación", "calma"),
    ("Me siento en sintonía con el universo", "calma"),
    ("Agradezco estar vivo un día más", "calma"),
    ("Todo está justo donde debe estar", "calma"),
    ("Me tomé un té y me siento renovado", "calma"),
    ("No necesito nada más para ser feliz ahora", "calma"),
    ("Observar las nubes me trajo mucha paz", "calma"),
    ("Siento una tranquilidad profunda en mi ser", "calma"),
    ("He aceptado las cosas que no puedo cambiar", "calma"),
    
    # CONFUSIÓN (Nueva categoría)
    ("No sé qué camino tomar", "confusion"),
    ("Me siento perdido, no sé quién soy", "confusion"),
    ("No sé si tomé la decisión correcta", "confusion"),
    ("Me siento perdido en un laberinto", "confusion"),
    ("Tengo tantas opciones que me bloqueo", "confusion"),
    ("No entiendo qué esperan de mí", "confusion"),
    ("Todo es muy borroso en mi mente ahora", "confusion"),
    ("¿Quién soy realmente?", "confusion"),
    ("Siento que camino sin rumbo fijo", "confusion"),
    ("Mis pensamientos se contradicen todo el tiempo", "confusion"),
    
    
    # --- LOTE 2: PROFUNDIDAD Y MATICES (Copia desde aquí) ---
    # TRISTEZA (Soledad y Nostalgia)
    ("Me duele mucho ver fotos viejas y recordar lo que perdí", "tristeza"),
    ("Siento que nadie nota si estoy o no estoy", "tristeza"),
    ("La soledad en esta casa se siente insoportable hoy", "tristeza"),
    ("He perdido la motivación para seguir mis sueños", "tristeza"),
    ("Siento que fallé y no hay vuelta atrás", "tristeza"),
    ("Cada día se siente igual de gris y pesado", "tristeza"),
    ("Extraño a alguien que ya no va a volver", "tristeza"),
    ("Tengo un dolor en el alma que no sé explicar", "tristeza"),
    ("A veces desearía simplemente desaparecer un rato", "tristeza"),
    ("Me siento desconectado de todos mis amigos", "tristeza"),

    # ANSIEDAD (Social y Presión)
    ("Siento que todos me miran y me juzgan cuando hablo", "ansiedad"),
    ("Tengo miedo de decir algo estúpido y arruinarlo todo", "ansiedad"),
    ("La presión del trabajo me está matando", "ansiedad"),
    ("No puedo dormir pensando en los pendientes de mañana", "ansiedad"),
    ("Siento que el tiempo se me acaba y no he hecho nada", "ansiedad"),
    ("Me da pánico recibir llamadas de números desconocidos", "ansiedad"),
    ("Siento una opresión en el pecho cuando pienso en dinero", "ansiedad"),
    ("Tengo miedo de enfermarme o que algo le pase a mi familia", "ansiedad"),
    ("No puedo quedarme quieto, necesito hacer algo ya", "ansiedad"),
    ("Me siento atrapado y sin salida en esta situación", "ansiedad"),

    # IRA (Injusticia y Trabajo)
    ("Mi jefe no valora mi esfuerzo y eso me enfurece", "ira"),
    ("Me robaron el crédito por algo que yo hice", "ira"),
    ("Odio tener que repetir las cosas mil veces", "ira"),
    ("Es injusto que siempre ganen los mentirosos", "ira"),
    ("Me da mucha rabia el tráfico y perder mi tiempo", "ira"),
    ("No soporto que me interrumpan cuando estoy hablando", "ira"),
    ("Me siento traicionado por alguien en quien confiaba", "ira"),
    ("Tengo ganas de mandarlo todo al diablo", "ira"),
    ("Estoy cansado de ser siempre el que cede", "ira"),
    ("La incompetencia de los demás me saca de quicio", "ira"),

    # CALMA (Naturaleza y Aceptación)
    ("El sonido de la lluvia me hace sentir muy tranquilo", "calma"),
    ("Hoy decido no preocuparme por lo que no puedo controlar", "calma"),
    ("Me siento ligero, como si me hubiera quitado un peso de encima", "calma"),
    ("Disfruto simplemente estando aquí y ahora", "calma"),
    ("He perdonado y me siento libre", "calma"),
    ("La brisa fresca en mi cara me reconforta", "calma"),
    ("No tengo prisa, llegaré cuando tenga que llegar", "calma"),
    ("Siento una calidez agradable en mi interior", "calma"),
    ("Todo tiene su momento bajo el sol", "calma"),
    ("Estoy agradecido por las pequeñas cosas de hoy", "calma"),

    # CONFUSIÓN Y DUDA (Existencial)
    ("No entiendo por qué la gente actúa como actúa", "confusion"),
    ("Siento que todo lo que creía saber es mentira", "confusion"),
    ("No sé si debo seguir luchando o rendirme", "confusion"),
    ("Mi cabeza es un caos de ideas contradictorias", "confusion"),
    ("¿Cuál es el propósito de todo esto?", "confusion"),
    ("Me siento dividido entre dos caminos", "confusion"),
    ("No logro ver con claridad mi futuro", "confusion"),
    ("Tengo preguntas que nadie sabe responderme", "confusion"),
    # --- FIN LOTE 2 ---
    
    # --- LOTE 3: MODISMOS Y EXPRESIONES INTENSAS (Copia desde aquí) ---
    # TRISTEZA (Expresiones fuertes/vulgares)
    ("Me siento de la verga hoy", "tristeza"),
    ("Todo me sale de la chingada", "tristeza"),
    ("Ando bien agüitado, no quiero nada", "tristeza"),
    ("La neta me siento dlv (de la verga)", "tristeza"),
    ("Siento que valgo madre en la vida", "tristeza"),
    ("Me lleva la que me trajo, qué tristeza", "tristeza"),
    ("Ando bajoneado, todo está pinche gris", "tristeza"),
    ("Me siento culero, la verdad", "tristeza"),
    ("Siento un hueco bien cabrón en el pecho", "tristeza"),
    ("La vida me está tratando de la patada", "tristeza"),

    # IRA (Enojo explosivo)
    ("Estoy emputado con todo el mundo", "ira"),
    ("Me tienen hasta la madre con sus pendejadas", "ira"),
    ("Me caga que no me salgan las cosas", "ira"),
    ("Chinga su madre, ya no aguanto más", "ira"),
    ("Qué pinche coraje tengo atorado", "ira"),
    ("Me reencabrona la gente mentirosa", "ira"),
    ("Tengo ganas de mandar todo a la goma", "ira"),
    ("Me hierve la sangre, no mames", "ira"),
    ("Estoy que me lleva la chingada del coraje", "ira"),
    ("Pinche día asqueroso que llevo", "ira"),

    # ANSIEDAD (Malviaje y Pánico)
    ("Me estoy malviajando bien feo", "ansiedad"),
    ("Siento que me va a dar el patatús", "ansiedad"),
    ("Ando bien paniqueado por lo que pasó", "ansiedad"),
    ("Siento la cabeza hecha un desmadre", "ansiedad"),
    ("Me siento bien pinche nervioso sin razón", "ansiedad"),
    ("Traigo un nudo culero en la garganta", "ansiedad"),
    ("Me está cargando el payaso con tanta presión", "ansiedad"),
    ("No puedo ni tragar del pinche estrés", "ansiedad"),
    ("Siento que voy a valer madre en el examen", "ansiedad"),
    ("Me siento asfixiado, está cabrón", "ansiedad"),

    # CANSANCIO (Hartazgo total)
    ("Estoy hasta el huevo de trabajar", "cansancio"),
    ("Ya no jalo, necesito dormir una semana", "cansancio"),
    ("Ando bien madreado, me duele todo", "cansancio"),
    ("Me siento hecho mierda físicamente", "cansancio"),
    ("Ya dio lo que tenía que dar, estoy fundido", "cansancio"),
    ("Estoy molido, ya no doy una", "cansancio"),
    ("Me siento como trapo viejo, bien gastado", "cansancio"),
    ("La neta ya no tengo pila para nada", "cansancio"),
    ("Estoy que me caigo de sueño, al chile", "cansancio"),
    ("Qué hueva de vida, estoy agotadísimo", "cansancio"),

    # CONFUSIÓN (Duda existencial coloquial)
    ("No sé qué pedo con mi vida", "confusion"),
    ("Ando bien norteado, no sé pa dónde darle", "confusion"),
    ("No entiendo ni madres de lo que pasa", "confusion"),
    ("Me siento sacado de onda", "confusion"),
    ("Qué pedo, todo cambió de repente", "confusion"),
    ("No sé si cagarla o quedarme quieto", "confusion"),
    # --- FIN LOTE 3 ---
    
    # --- LOTE 4: RELACIONES, CULPA Y APATÍA (Copia desde aquí) ---
    
    # TRISTEZA (Desamor y Ruptura)
    ("Ella me dejó y no sé cómo seguir", "tristeza"),
    ("Terminé con mi pareja y me siento vacío", "tristeza"),
    ("Extraño sus mensajes de buenos días", "tristeza"),
    ("Siento que perdí al amor de mi vida", "tristeza"),
    ("Verla con otro me destroza el alma", "tristeza"),
    ("Me duele pensar que ya no somos nada", "tristeza"),
    ("Nuestro aniversario ya no significa nada", "tristeza"),
    ("Tengo el corazón hecho pedazos por su culpa", "tristeza"),
    ("Ya no creo en el amor, me rindo", "tristeza"),
    ("Me siento usado y desechado", "tristeza"),

    # TRISTEZA (Culpa y Arrepentimiento)
    ("Me siento fatal por lo que dije ayer", "tristeza"),
    ("La cagué horrible y no sé cómo arreglarlo", "tristeza"),
    ("Me arrepiento de no haber estado ahí", "tristeza"),
    ("Siento que soy una mala persona", "tristeza"),
    ("No me perdono haberle fallado así", "tristeza"),
    ("Cargo con una culpa que no me deja vivir", "tristeza"),
    ("Ojalá pudiera regresar el tiempo y cambiarlo", "tristeza"),
    ("Me siento sucio por lo que hice", "tristeza"),
    
    # IRA (Envidia y Celos)
    ("Me caga que a él le vaya bien y a mí no", "ira"),
    ("Es injusto que ella tenga todo tan fácil", "ira"),
    ("Me da rabia verlos felices mientras yo sufro", "ira"),
    ("Odio que siempre lo prefieran a él", "ira"),
    ("Me revienta que presuma su dinero", "ira"),
    ("¿Por qué la vida le sonríe a los idiotas?", "ira"),
    ("Me dan celos enfermizos cuando sale", "ira"),
    ("Me molesta que nadie reconozca mi talento", "ira"),
    ("Maldita sea mi suerte comparada con la suya", "ira"),
    
    # ANSIEDAD (Inseguridad y Síndrome del Impostor)
    ("Siento que soy un fraude y se van a dar cuenta", "ansiedad"),
    ("Me da pánico que descubran que no sé nada", "ansiedad"),
    ("Siento que no merezco estar aquí", "ansiedad"),
    ("Tengo miedo de no estar a la altura", "ansiedad"),
    ("Me comparo con todos y siempre pierdo", "ansiedad"),
    ("Me aterra hablar en público, me bloqueo", "ansiedad"),
    ("Siento que todos se ríen de mí a mis espaldas", "ansiedad"),
    ("Tengo miedo de quedarme pobre", "ansiedad"),

    # CANSANCIO (Apatía y Desmotivación)
    ("Todo me da igual, me importa un carajo", "cansancio"),
    ("No tengo ganas ni de levantarme a comer", "cansancio"),
    ("La vida me sabe a cartón, no disfruto nada", "cansancio"),
    ("Hago las cosas por inercia, soy un robot", "cansancio"),
    ("Me da hueva hasta hablar con mis amigos", "cansancio"),
    ("Simplemente no le veo el punto a esforzarme", "cansancio"),
    ("Estoy en piloto automático todo el día", "cansancio"),
    ("Me siento gris, ni feliz ni triste, solo apagado", "cansancio"),
    # --- FIN LOTE 4 ---
    
    # --- LOTE 5: DUELO, TRAICIÓN Y VIDA MODERNA (Copia desde aquí) ---

    # TRISTEZA (Duelo y Pérdida profunda)
    ("Falleció alguien muy importante para mí y no lo acepto", "tristeza"),
    ("Extraño demasiado a mi abuela, me hace mucha falta", "tristeza"),
    ("Perdí a mi mascota y la casa se siente vacía", "tristeza"),
    ("El luto me está consumiendo por dentro", "tristeza"),
    ("Siento que una parte de mí murió con él", "tristeza"),
    ("Ya no puedo llamar a mis padres y eso me mata", "tristeza"),
    ("La muerte es injusta, se llevó a quien más amaba", "tristeza"),
    ("No pude despedirme y cargo con ese dolor", "tristeza"),
    ("Ver su silla vacía me rompe el corazón cada día", "tristeza"),

    # ANSIEDAD (Tecnología y Agobio Digital)
    ("Las redes sociales me hacen sentir miserable e insuficiente", "ansiedad"),
    ("No puedo dejar de ver noticias horribles y me paniqueo", "ansiedad"),
    ("Siento que todos tienen vidas perfectas en Instagram menos yo", "ansiedad"),
    ("El celular no para de sonar y me pone de nervios", "ansiedad"),
    ("Necesito desconectarme pero tengo miedo de perderme algo", "ansiedad"),
    ("Tengo el cerebro frito de tanta información inútil", "ansiedad"),
    ("Me comparo con gente de internet y me siento basura", "ansiedad"),
    ("La tecnología me está robando la vida real", "ansiedad"),

    # IRA (Traición y Falsedad)
    ("Me apuñalaron por la espalda quienes decían ser mis amigos", "ira"),
    ("Descubrí que me estuvieron mintiendo todo este tiempo", "ira"),
    ("Me usaron para conseguir lo que querían y luego me botaron", "ira"),
    ("Odio a la gente doble cara, son unos hipócritas", "ira"),
    ("Le conté mi secreto y se lo dijo a todos", "ira"),
    ("Confié ciegamente y me vieron la cara de idiota", "ira"),
    ("No perdono la deslealtad, eso no se olvida", "ira"),
    ("Me da coraje haber sido tan ingenuo con esa persona", "ira"),

    # CANSANCIO (Burnout Creativo/Mental)
    ("Tengo la mente en blanco, no se me ocurre nada", "cansancio"),
    ("Me siento estancado, como si no avanzara nada", "cansancio"),
    ("Estoy bloqueado, intento trabajar y no puedo", "cansancio"),
    ("Mi creatividad se murió, estoy seco", "cansancio"),
    ("Forzarme a pensar me duele físicamente", "cansancio"),
    ("Necesito vacaciones de mi propio cerebro", "cansancio"),

    # CALMA (Renovación y Esperanza)
    ("Siento que hoy empieza un nuevo capítulo en mi vida", "calma"),
    ("Después de la tormenta, por fin veo la luz", "calma"),
    ("Me siento listo para volver a intentarlo con calma", "calma"),
    ("He limpiado mi espacio y mi mente se siente clara", "calma"),
    ("Tengo esperanza de que todo se acomodará", "calma"),
    ("Me siento fresco y con energía renovada", "calma"),
    ("He soltado lo viejo para dejar entrar lo nuevo", "calma")
    # --- FIN LOTE 5 ---

    # =================================================================
    #  VVVV  AQUÍ PEGA LOS SIGUIENTES LOTES (LOTE 2, LOTE 3...)  VVVV
    # =================================================================
    
    # (Pega aquí el Lote 2...)

    # =================================================================
]


# 2. LAS CITAS (Base de datos de sabiduría extendida)
# -----------------------------------------------------------------
citas_db = {
    "tristeza": [
        # Las que ya tenías:
        "“El camino que puede ser nombrado no es el camino eterno.” — Tao Te Ching",
        "“La tristeza es como la lluvia; déjala caer, nutrirá las semillas de tu crecimiento.” — Proverbio Zen",
        "“Vacía tu mente de todo pensamiento. Deja que tu corazón esté en paz.” — Laozi",
        "“Incluso la noche más oscura terminará y el sol saldrá.” — Victor Hugo",
        # NUEVAS (Lote 1):
        "“La gran tierra me carga con un cuerpo, me hace trabajar con la vida, me alivia con la vejez y me da descanso en la muerte.” — Zhuangzi",
        "“Lo que la oruga llama el fin del mundo, el resto del mundo lo llama mariposa.” — Laozi",
        "“El dolor es inevitable, pero el sufrimiento es opcional.” — Proverbio Budista",
        "“No puedes evitar que las aves de la tristeza vuelen sobre tu cabeza, pero puedes evitar que aniden en tu cabello.” — Proverbio Chino",
        "“Todo lo que tiene un principio tiene un fin. Haz las paces con eso y todo estará bien.” — Jack Kornfield",
        "“El árbol que quiere tocar el cielo debe tener raíces que lleguen hasta el infierno.” — Carl Jung (Influencia Taoísta)"
    ],
    "ansiedad": [
        # Las que ya tenías:
        "“El hombre perfecto usa su mente como un espejo: no agarra nada, no rechaza nada.” — Zhuangzi",
        "“Si estás deprimido, vives en el pasado. Si estás ansioso, vives en el futuro. Si estás en paz, vives en el presente.” — Laozi",
        "“Preocúpate por lo que piensan los demás y siempre serás su prisionero.” — Laozi",
        "“La tensión es quien crees que deberías ser. La relajación es quien eres.” — Proverbio Chino",
        # NUEVAS (Lote 1):
        "“Quien pretende el dominio del mundo y mejorar este, se encamina al fracaso. El mundo es tan sagrado que no puede ser dominado.” — Tao Te Ching",
        "“El que camina a grandes zancadas no irá muy lejos.” — Laozi",
        "“Si no cambias la dirección, puedes terminar donde has comenzado.” — Laozi",
        "“No habites en el pasado, no sueñes con el futuro, concentra la mente en el momento presente.” — Buda",
        "“Tienes el poder sobre tu mente, no sobre los eventos externos. Date cuenta de esto y encontrarás fuerza.” — Marco Aurelio (Estoicismo, muy compatible)"
    ],
    "calma": [
        # Las que ya tenías:
        "“La paz viene de dentro. No la busques fuera.” — Buda",
        "“El que está satisfecho con su parte es rico.” — Laozi",
        "“Al igual que una roca sólida no se mueve con el viento, los sabios no se inmutan por el elogio o la culpa.”",
        "“La naturaleza no se apresura, y sin embargo todo se logra.” — Laozi",
        # NUEVAS (Lote 1):
        "“El silencio es una fuente de gran fuerza.” — Laozi",
        "“Reposar es volver a su destino. Volver al destino es conocer la eternidad.” — Tao Te Ching",
        "“Sé como el agua: suave y flexible, pero capaz de erosionar la roca más dura.” — Laozi",
        "“Quédate sentado en silencio, sin hacer nada, y la primavera llega y la hierba crece sola.” — Proverbio Zen",
        "“La calma somete a lo agitado.” — Laozi"
    ],
    "ira": [
        # Las que ya tenías:
        "“El que domina a los otros es fuerte; el que se domina a sí mismo es poderoso.” — Tao Te Ching",
        "“Aferrarse a la ira es como beber veneno y esperar que la otra persona muera.” — Buda",
        "“La mejor respuesta a la ira es el silencio.”",
        "“Quien es capaz de dominarse a sí mismo cuando está enojado, ha vencido a su peor enemigo.”",
        # NUEVAS (Lote 1):
        "“La violencia, aunque bien intencionada, siempre rebota sobre uno mismo.” — Laozi",
        "“El buen hombre es el maestro del malo, y el mal hombre es la lección del buen hombre.” — Tao Te Ching",
        "“Lo suave y lo tierno vencen a lo duro y lo grosero.” — Laozi",
        "“Si alguien te ofrece un regalo (insulto) y tú no lo aceptas, ¿a quién pertenece el regalo?” — Buda",
        "“No te resistas, eso solo crea dolor. Deja que la realidad sea la realidad.” — Laozi"
    ],
    "confusion": [
        # Las que ya tenías:
        "“El barro fangoso se aclara si se deja reposar. La mente confusa se aclara si se deja en paz.”",
        "“No busques, no busques, no preguntes, no llames, no demandes. Relájate.” — Osho",
        "“El viaje de mil millas comienza con un solo paso.” — Laozi",
        "“Cuando el alumno está listo, el maestro aparece.”",
        # NUEVAS (Lote 1):
        "“Darte cuenta de que no entiendes es una virtud; no darte cuenta de que no entiendes es un defecto.” — Laozi",
        "“El que sabe, no habla; el que habla, no sabe.” — Tao Te Ching",
        "“Perfecto viajero es el que no sabe adónde va.” — Liezi",
        "“El sabio no enseña con palabras, sino con actos.” — Laozi"
    ],
    "cansancio": [
        # Las que ya tenías:
        "“Aprende a descansar, no a renunciar.”",
        "“El arco que se mantiene siempre tenso, termina rompiéndose.”",
        "“Tomarse un descanso es parte del camino, no el final del mismo.”",
        # NUEVAS (Lote 1):
        "“Retirarse cuando la obra está hecha, ese es el camino del Cielo.” — Tao Te Ching",
        "“Correr siete veces y sentarse una vez.” — Proverbio Zen",
        "“Parar al menos una vez cada día para mirarte a ti mismo.” — Proverbio Chino",
        "“Haz las cosas difíciles mientras son fáciles y haz las grandes cosas mientras son pequeñas.” — Laozi (Prevención del agobio)"
    ],
    
    "tristeza": [
        # --- LOTE 2 (Nuevas) ---
        "“No puedes evitar que las aves de la tristeza vuelen sobre tu cabeza, pero puedes evitar que aniden en tu cabello.” — Proverbio Chino",
        "“La vida es un préstamo; la muerte es el regreso al origen. ¿Por qué estar triste por volver a casa?” — Liezi",
        "“Todo lo que nace vuelve a lo sin forma. Acepta el ciclo y el dolor se desvanecerá.” — Liezi",
        "“El que conoce a los demás es sabio; el que se conoce a sí mismo está iluminado.” — Laozi",
        "“Suelta lo que crees que debes ser y abraza lo que eres.” — Brené Brown (Adaptación Taoísta)",
        "“El dolor es la ruptura del caparazón que encierra tu entendimiento.” — Kahlil Gibran"
    ],
    "ansiedad": [
         # --- LOTE 2 (Nuevas) ---
        "“Si te deprimes, vives en el pasado. Si te ansías, vives en el futuro. Si estás en paz, vives en el presente.” — Laozi",
        "“El hombre que persigue dos conejos, no atrapa ninguno.” — Proverbio Chino",
        "“¿Tienes paciencia para esperar a que tu lodo se asiente y el agua se aclare?” — Tao Te Ching",
        "“No empujes el río, fluye solo.” — Barry Stevens",
        "“La preocupación no quita los problemas de mañana, solo quita la paz de hoy.” — Proverbio Zen"
    ],
    "calma": [
         # --- LOTE 2 (Nuevas) ---
        "“Siéntate en silencio, no hagas nada, la primavera llega y la hierba crece sola.” — Proverbio Zen",
        "“La respuesta más silenciosa es a veces la más ruidosa.”",
        "“El sabio no acumula. Cuanto más ayuda a los demás, más se beneficia él mismo.” — Laozi",
        "“La simplicidad es la máxima sofisticación.” — Laozi (Atribuido)",
        "“Cuando bebes agua, recuerda la fuente.” — Proverbio Chino"
    ],
    "ira": [
         # --- LOTE 2 (Nuevas) ---
        "“Es más fácil desviar el curso de un río que cambiar el carácter de un hombre necio. No te desgastes.” — Proverbio Chino",
        "“El que golpea primero admite que se le acabaron las ideas.” — Proverbio Chino",
        "“No hables si lo que vas a decir no es más hermoso que el silencio.”",
        "“La violencia, incluso cuando es bien intencionada, siempre rebota sobre uno mismo.” — Laozi",
        "“Sé como el sándalo, que perfuma el hacha que lo hiere.” — Proverbio Hindú/Zen"
    ],
    "confusion": [
         # --- LOTE 2 (Nuevas) ---
        "“Solo los que conocen el valor de lo inútil pueden hablar de lo que es útil.” — Zhuangzi (Sobre no obsesionarse con la productividad)",
        "“El perfecto viajero es el que no sabe adónde va.” — Liezi",
        "“Todos los hombres conocen la utilidad de lo útil, pero nadie conoce la utilidad de lo inútil.” — Zhuangzi",
        "“Un viaje de mil millas comienza con un solo paso.” — Laozi",
        "“Cuando el ojo no está bloqueado, el resultado es la visión. Cuando la mente no está bloqueada, el resultado es la sabiduría.” — Proverbio Zen"
    ],
    "cansancio": [
         # --- LOTE 2 (Nuevas) ---
        "“Nadar contra la corriente agota; flotar con ella renueva.” — Principio Wu Wei",
        "“Retirarse cuando la obra está hecha, ese es el camino del Cielo.” — Tao Te Ching",
        "“El arco que siempre está tenso termina por romperse.” — Proverbio Chino",
        "“Haz las cosas difíciles mientras son fáciles y haz las grandes cosas mientras son pequeñas.” — Laozi (Para evitar el agobio)",
        "“Correr siete veces y sentarse una vez es también avanzar.” — Proverbio Zen"
    ],
    
    "tristeza": [
        # --- LOTE 3 (Relaciones y Apego) ---
        "“Si quieres conservar algo, debes admitir que puedes perderlo.” — Liezi",
        "“El que ama a los demás es constantemente amado por ellos; el que respeta a los demás es constantemente respetado.” — Mencio (Filosofía oriental afín)",
        "“Si un bote vacío choca contra ti, no te enojas. Si hay alguien dentro, le gritas. Vacía tu bote (tu ego) y nadie se opondrá a ti.” — Zhuangzi (Parábola del Bote Vacío)",
        "“La oruga llama fin del mundo a lo que el maestro llama mariposa. A veces el final es solo una transformación.” — Richard Bach (Vibe Taoísta)",
        "“No retengas lo que se va, no rechaces lo que llega.” — Proverbio Zen"
    ],
    "ansiedad": [
         # --- LOTE 3 (Dinero y Futuro) ---
        "“Si llenas tu casa de oro y jade, no podrás protegerla; el que acumula riqueza y honores siembra su propia desgracia.” — Tao Te Ching",
        "“Quien sabe que tiene suficiente es rico.” — Laozi",
        "“El que persigue la fama pierde su identidad; el que persigue la fortuna pierde su alma.” — Proverbio Chino",
        "“La felicidad no está en tener mucho, sino en necesitar poco.” — Liezi",
        "“Preocuparse es rezar por lo que no quieres.” — Proverbio Zen"
    ],
    "calma": [
         # --- LOTE 3 (Contra el Caos) ---
        "“El agua turbia se aclara dejándola quieta.” — Laozi",
        "“Sé como el bambú: cuanto más alto crece, más se inclina (humildad).” — Proverbio Chino",
        "“Cuando dejas de buscar aprobación, la encuentras.” — Tao Te Ching",
        "“La libertad suprema es no sentir la necesidad de explicar quién eres.”"
    ],
    "ira": [
         # --- LOTE 3 (Envidia y Personas Tóxicas) ---
        "“El que se para de puntillas no se mantiene firme; el que se exhibe no brilla.” — Tao Te Ching (Para la gente presumida)",
        "“Nunca luches con un cerdo. Ambos se ensuciarán, pero al cerdo le gustará.” — George Bernard Shaw (Muy aplicable aquí)",
        "“Si alguien te ofrece un insulto y tú no lo aceptas, ¿a quién pertenece el insulto? Al que lo ofreció.” — Buda",
        "“La mejor venganza es no ser como tu enemigo.” — Marco Aurelio (Estoicismo/Taoísmo universal)",
        "“El árbol que tiene las flores más bellas y los frutos más dulces es el primero al que le tiran piedras.” — Proverbio Oriental (Sobre la envidia)"
    ],
    "confusion": [
         # --- LOTE 3 (Falsedad Social) ---
        "“La fama es el comienzo de la desgracia.” — Zhuangzi",
        "“El pez que se mantiene en aguas profundas no puede ser pescado; el hombre que guarda su misterio no puede ser manipulado.”",
        "“Conocer a otros es inteligencia; conocerse a sí mismo es verdadera sabiduría. Dominar a otros es fuerza; dominarse a sí mismo es verdadero poder.” — Laozi"
    ],
    "cansancio": [
         # --- LOTE 3 (Burnout y Trabajo) ---
        "“El hombre que mueve montañas empieza apartando piedrecitas.” — Confucio",
        "“No hay mayor delito que la codicia; no hay mayor desgracia que no saber contentarse.” — Laozi",
        "“Una vela no pierde su luz por compartirla con otra, pero se consume si arde demasiado rápido.”"
    ],
    "tristeza": [
        # --- LOTE 5 (Aceptación del Cambio) ---
        "“Aquello que para la oruga es el fin del mundo, para el resto del mundo se llama mariposa.” — Laozi",
        "“La vida es una serie de cambios naturales. No te resistas a ellos, eso solo crea dolor.” — Laozi",
        "“Si un árbol cae en el bosque, se convierte en abono para el nuevo bosque. Tu caída también nutre tu futuro.” — Proverbio Zen",
        "“El dolor es inevitable, el sufrimiento es opcional.” — Proverbio Budista",
        "“Lo que niegas te somete, lo que aceptas te transforma.” — Carl Jung (Filosofía muy Taoísta)"
    ],
    "ansiedad": [
         # --- LOTE 5 (Prisa y Perfeccionismo) ---
        "“La naturaleza no se apresura, y sin embargo todo se logra.” — Laozi (Clave para la ansiedad)",
        "“Si quieres enderezar lo curvo, primero debes dejar que se curve completamente.” — Tao Te Ching",
        "“El hombre que persigue la perfección camina hacia la decepción constante.” — Zhuangzi",
        "“Un viaje de mil millas comienza con un solo paso. No intentes saltarte el camino.” — Laozi",
        "“Preocuparse es como caminar con un paraguas abierto esperando a que llueva.” — Proverbio Zen"
    ],
    "calma": [
         # --- LOTE 5 (Simplicidad) ---
        "“Solo tengo tres tesoros que guardar: simplicidad, paciencia y compasión.” — Laozi",
        "“Sé como el agua: se adapta al recipiente sin perder su esencia.” — Tao Te Ching",
        "“La riqueza consiste en mucho más que tener oro; consiste en apreciar lo que ya tienes.” — Liezi",
        "“Quédate en el centro del círculo y deja que todas las cosas sigan su curso.” — Tao Te Ching"
    ],
    "ira": [
         # --- LOTE 5 (Control y Liderazgo) ---
        "“Para conducir a la gente, camina detrás de ellos.” — Laozi",
        "“El que golpea primero admite que se le acabaron las ideas.” — Proverbio Chino",
        "“Responder a la ira con ira es como lanzar leña al fuego. Responder con silencio es quitarle el oxígeno.”",
        "“Si alguien te escupe, agradécele por limpiar tu cara. Si te insulta, agradécele por limpiar tu ego.” — Adaptación Zen"
    ],
    "confusion": [
         # --- LOTE 5 (Intuición y No-Saber) ---
        "“El sabio viaja todo el día sin dejar su propia casa.” — Laozi (Sobre viajar hacia adentro)",
        "“Deja de pensar y terminarán tus problemas.” — Tao Te Ching",
        "“No busques la verdad; solo deja de tener opiniones.” — Proverbio Zen",
        "“El conocimiento es aprender algo cada día. La sabiduría es soltar algo cada día.” — Proverbio Zen"
    ],
    "cansancio": [
         # --- LOTE 5 (Rendirse vs Descansar) ---
        "“No te rindas, descansa. El campo que descansa da mejor cosecha.” — Proverbio Chino",
        "“Incluso el río más caudaloso necesita una llanura para calmarse.”",
        "“Hacer nada es mejor que estar ocupado haciendo nada.” — Laozi (Sobre el trabajo inútil)"
    ]
}
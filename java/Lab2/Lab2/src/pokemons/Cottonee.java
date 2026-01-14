package pokemons;

import attacks.status.Growth;
import attacks.status.Rest;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;
import attacks.status.Swagger;

public class Cottonee extends Pokemon {
    public Cottonee(String name, int lvl) {
        super(name, lvl);
        setStats(40.0, 27.0, 60.0, 37.0, 50.0, 66.0);
        setType(Type.GRASS, Type.FAIRY);
        setMove(new Swagger());
        setMove(new Growth());
        setMove(new Rest());
    }
}

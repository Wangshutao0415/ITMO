package attacks.status;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class RockTomb extends StatusMove {
    public RockTomb() {
        super(Type.ROCK, 60, 95.0);
    }
    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        pokemon.setMod(Stat.SPEED, -1);
    }
    @Override
    protected String describe() {
        return "Used RockTomb";
    }
}

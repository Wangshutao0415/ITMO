package attacks.status;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class Growth extends StatusMove {
    public Growth() {
        super(Type.NORMAL, 0.0, 100.0);
    }

    @Override
    protected void applySelfEffects(Pokemon pokemon) {
        pokemon.setMod(Stat.ATTACK, 1);
        pokemon.setMod(Stat.SPECIAL_ATTACK, 1);
    }

    @Override
    protected String describe() {
        return "Used Growth";
    }
}

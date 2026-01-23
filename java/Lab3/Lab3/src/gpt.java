//import Animal.Animal;
//
//public class Player {
//    private int gunpowder;
//    private int meat;
//    private int huntedCount;
//
//    public Player(int gunpowder) {
//        this.gunpowder = gunpowder;
//        this.meat = 0;
//        this.huntedCount = 0;
//    }
//
//    /**
//     * AI 版本捕猎方法
//     * 功能完整，但逻辑稍长，可读性比自己的版本略低
//     */
//    public void hunt(Animal animal) {
//        if (animal == null) {
//            System.out.println("AI: No animal to hunt.");
//            return;
//        }
//
//        int cost = animal.getGunpowderCost();
//
//        // AI 风格：先打印一大段信息，再判断
//        System.out.println("[AI] Preparing to hunt " + animal.getName());
//        System.out.println("[AI] Current gunpowder: " + gunpowder + ", Meat: " + meat);
//
//        if (gunpowder < cost) {
//            System.out.println("[AI] Cannot hunt " + animal.getName() + ". Not enough gunpowder.");
//            return;
//        }
//
//        // 执行捕猎
//        HuntAction action = new HuntAction();
//        action.execute(this, animal);
//
//        huntedCount++;
//        System.out.println("[AI] Successfully hunted " + animal.getName());
//        System.out.println("[AI] Gunpowder left: " + gunpowder + ", Total meat: " + meat);
//    }
//
//    public void addMeat(int amount) {
//        meat += amount;
//    }
//
//    public void consumeGunpowder(int amount) {
//        gunpowder -= amount;
//    }
//
//    public int getHuntedCount() {
//        return huntedCount;
//    }
//
//    public int getMeat() {
//        return meat;
//    }
//
//    public int getGunpowder() {
//        return gunpowder;
//    }
//}

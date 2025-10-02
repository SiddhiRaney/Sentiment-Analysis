class Solution {
public:
    static int maxBottlesDrunk(int totalBottles, int exchangeRate) {
        int bottlesDrunk = totalBottles;
        int emptyBottles = totalBottles;

        while (emptyBottles >= exchangeRate) {
            int newBottles = emptyBottles / exchangeRate; // number of new bottles from exchange
            bottlesDrunk += newBottles;
            emptyBottles = emptyBottles % exchangeRate + newBottles; // leftover + new empty
        }

        return bottlesDrunk;
    }
};

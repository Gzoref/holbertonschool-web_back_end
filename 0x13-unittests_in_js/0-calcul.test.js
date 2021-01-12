const assert = require("assert");
const calculateNumber = require("./0-calcul");

describe("calculateNumber", function () {
  describe("Two numbers", function () {
    it("should return 4", function () {
      assert.equal(calculateNumber(1, 3), 4);
    });
  });

  describe("one rounded number", function () {
    it("should return 5", function () {
      assert.equal(calculateNumber(1, 3.7), 5);
    });
  });

  describe("two rounded numbers", function () {
    it("should return 5", function () {
      assert.equal(calculateNumber(1.2, 3.7), 5);
    });
  });

  describe("two rounded numbers", function () {
    it("should return 6", function () {
      assert.equal(calculateNumber(1.5, 3.7), 6);
    });
  });
});

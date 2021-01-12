const calculateNumber = require("./2-calcul_chai");
const chai = require("chai");
const expect = chai.expect;

describe("calculateNumber", function () {
  describe("Two numbers", function () {
    it("should return 6", function () {
      chai.expect(calculateNumber("SUM", 1.4, 4.5)).to.equal(6);
    });
  });

  describe("Two numbers", function () {
    it("should return -4", function () {
      chai.expect(calculateNumber("SUBTRACT", 1.4, 4.5)).to.equal(4);
    });
  });

  describe("Two numbers", function () {
    it("should return 0.2", function () {
      chai.expect(calculateNumber("DIVIDE", 1.4, 4.5)).to.equal(0.2);
    });
  });

  describe("Two numbers", function () {
    it("should return divide by 0 Error", function () {
      chai.expect(calculateNumber("DIVIDE", 1.4, 0)).to.equal("Error");
    });
  });
});

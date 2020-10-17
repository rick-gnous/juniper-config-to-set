/**
 * Parse a Juniper conf into a series of set commands
 *
 * Tim Price writes the parser in PHP (https://github.com/pgnuta/juniper-config-to-set)
 * and I just rewrite it in JS with HTML frontend.
 *
 * @author Tim Price | rick@gnous.eu
 * @licence GPL3
 */
class ParserJuniper {
  constructor() {
    this.tree = [];
  }

  resetTree() {
    this.tree = [];
  }

  /**
   * Concatenate all item of the tree
   *
   * @return {String} the string with all items
   */
  printTree() {
    let ret = "";
    this.tree.forEach(function(item, index, array) {
      ret = item + ret;
    });
    return ret;
  }

  /**
   * Parse a line of juniper conf
   *
   * @param {String} line - line of juniper conf
   * @return {String} a set command for line or an empty String if it’s comment
   */
  parse(line) {
    let ret = "";
    line = line.trim();
    if (line.charAt(0) !== '#') {
      if (line.includes('#')) {
        line = line.split('#')[0].trim();
      }

      let idEndline = line.length - 1;
      if (line.charAt(idEndline) === ';') {
        line = line.slice(0, -1);

        if (this.tree.length === 0) {
          ret = "set " + line;
        } else {
          ret = "set " + this.printTree() + line;
        }
      }

      if (line.charAt(idEndline) === '{') {
        line = line.slice(0, -1);
        this.tree.unshift(line);
      }

      if (line.charAt(idEndline) === '}') {
        this.tree.shift();
      }
    }
    return ret;
  }

  /**
   * Parse all lines of the text
   *
   * @param {String} text - juniper conf
   * @return {String} series of set commands
   */
  parseTxt(text) {
    this.resetTree();
    let ret = "";
    let lineConf;
    text = text.split("\n");
    for(let i = 0; i < text.length; i++) {
      lineConf = this.parse(text[i]);
      if (lineConf !== "") {
        ret += lineConf + "\n";
      }
    }
    return ret;
  }
}

const parser = new ParserJuniper();

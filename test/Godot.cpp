#include <Godot.hpp>
#include <Array.hpp>
#include "MatrixOperations.hpp"

using namespace godot;

class MatrixOperations : public Reference {
    GODOT_CLASS(MatrixOperations, Reference)

private:
    static void validateMatrixSize(Array matrix, int rows, int cols) {
        ERR_FAIL_COND_MSG(matrix.size() != rows, "Invalid number of rows in the matrix.");
        for (int i = 0; i < rows; i++) {
            ERR_FAIL_COND_MSG(matrix[i].size() != cols, "Invalid number of columns in row " + String(i) + ".");
        }
    }

public:
    static void _register_methods() {
        godot_methods::register_method("MatrixOperations", "add_matrices", &MatrixOperations::addMatrices);
    }

    static void addMatrices(Array a, Array b, Array result) {
        int rows = a.size();
        int cols = a[0].size();
        validateMatrixSize(b, rows, cols);

        for (int i = 0; i < rows; i++) {
            Array rowA = a[i];
            Array rowB = b[i];
            Array rowResult;

            for (int j = 0; j < cols; j++) {
                int sum = (int)rowA[j] + (int)rowB[j];
                rowResult.append(sum);
            }

            result.append(rowResult);
        }
    }

    MatrixOperations() {
        // Initialize the registered methods
        _register_methods();
    }
};


# test_matrix_operations.gd
extends Node

func test_matrix_addition():
    var A = [[1, 2], [3, 4]]
    var B = [[5, 6], [7, 8]]
    var expected_result = [[6, 8], [10, 12]]
    var result = MatrixOperations.add_matrices(A, B, 2, 2)

    assert(result == expected_result, "Matrix addition passed")

//1.	Verify that the startup time of the Godot editor is within an acceptable range
describe("Godot Editor Launch Time", function() {
  it("Should launch within 10 seconds", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Download").click();
    cy.contains("Get Godot").click();
    cy.get(".download").click();
    cy.get(".progress-bar").should("be.visible");
    cy.get(".progress-bar").should("not.exist", { timeout: 10000 });
  });
});
//2.	Verify whether the project import function is normal
describe("Godot Project Import", function() {
  it("Should successfully import a sample project", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Sample Projects").click();
    cy.get(".project-card:first").click();
    cy.get(".download-button").click();
    cy.contains("Import Project").should("be.visible");
  });
});
//3.	Verify whether the script editor can save the script file
describe("Godot Script Editor", function() {
  it("Should save a script file", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Scripting").click();
    cy.contains("Getting Started").click();
    cy.get("button:contains('Save')").click();
    cy.contains("File saved").should("be.visible");
  });
});
//4.	Verify whether the node editing function is normal
describe("Godot Node Editing", function() {
  it("Should add a new node", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Node").click();
    cy.get("button:contains('Add Child Node')").click();
    cy.get(".node").should("have.length.gt", 0);
  });
});
//5.	Verify whether the resource import function is normal
describe("Godot Resource Import", function() {
  it("Should import a texture resource", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Resources").click();
    cy.contains("Textures").click();
    cy.get("button:contains('Import')").click();
    cy.contains("Select File").should("be.visible");
  });
});
//6.	Verify whether playback mode can be started
describe("Godot Play Mode", function() {
  it("Should start play mode", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Getting Started").click();
    cy.get("button:contains('Play Scene')").click();
    cy.contains("Playing in editor").should("be.visible");
  });
});
//7.	Verify that the version control integration is working properly
describe("Godot Version Control", function() {
  it("Should commit changes to a project", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Version Control").click();
    cy.contains("Git").click();
    cy.get("button:contains('Commit')").click();
    cy.contains("Commit Successful").should("be.visible");
  });
});
//8.	Verify that the animation editor can create and save animations
describe("Godot Animation Editor", function() {
  it("Should create and save an animation", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Animation").click();
    cy.contains("Creating an Animation").click();
    cy.get("button:contains('Save')").click();
    cy.contains("Animation saved").should("be.visible");
  });
});
//9.	Verify whether the script debugging function is normal
describe("Godot Script Debugging", function() {
  it("Should set breakpoints and debug a script", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Debugging").click();
    cy.get("button:contains('Toggle Breakpoint')").click();
    cy.get("button:contains('Debug')").click();
    cy.contains("Debugging session started").should("be.visible");
  });
});
//10.	Verify whether the export function is normal
describe("Godot Project Export", function() {
  it("Should successfully export a project", function() {
    cy.visit("https://godotengine.org/");
    cy.contains("Documentation").click();
    cy.contains("Exporting Projects").click();
    cy.get("button:contains('Export Project')").click();
    cy.contains("Export Successful").should("be.visible");
  });
});
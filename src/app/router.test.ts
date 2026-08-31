import { describe, it, expect } from "vitest";
import { pathToScreen, screenToPath, detectHostDefault } from "./router";

describe("router /login deep-link", () => {
  it("maps /login path to the login screen", () => {
    expect(pathToScreen("/login")).toBe("login");
  });

  it("maps /app/login path to the login screen", () => {
    expect(pathToScreen("/app/login")).toBe("login");
  });

  it("round-trips login screen to /login path", () => {
    expect(screenToPath("login")).toBe("/login");
  });

  it("keeps app-subdomain default for the app root", () => {
    expect(detectHostDefault()).toBeTruthy();
  });

  it("does not treat other /app routes as login", () => {
    expect(pathToScreen("/app")).toBe("learning-path");
    expect(pathToScreen("/app/module")).toBe("module");
  });
});

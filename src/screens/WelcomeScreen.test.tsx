import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { AppProvider } from "../app/AppProvider";
import { App } from "../app/App";

describe("WelcomeScreen", () => {
  beforeEach(() => localStorage.clear());

  it("renders a first-visit screen immediately", () => {
    render(<AppProvider><App /></AppProvider>);
    expect(document.querySelector(".loading-screen") || document.querySelector(".welcome-screen")).toBeTruthy();
  });

  it("shows the landing page", async () => {
    render(<AppProvider><App /></AppProvider>);
    expect(await screen.findByText("GramLingo", {}, { timeout: 3000 })).toBeInTheDocument();
    const buttons = screen.getAllByText("Start Learning");
    expect(buttons.length).toBeGreaterThanOrEqual(1);
    expect(screen.getByText(/Grammar Quest/)).toBeInTheDocument();
  });

  it("creates a new player via the login modal", async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    const startBtns = await screen.findAllByText("Start Learning", {}, { timeout: 3000 });
    await user.click(startBtns[0]);
    await user.click(screen.getByText("New Player"));
    await user.type(screen.getByPlaceholderText("Username"), "teststudent");
    await user.type(screen.getByPlaceholderText("PIN (optional)"), "1234");
    await user.click(screen.getByText("Log In"));
    expect(await screen.findByRole("button", { name: /Relative Clauses: Lesson plan/ })).toBeInTheDocument();
  });

  it("logs in an existing user via the modal", async () => {
    const user = userEvent.setup();
    render(<AppProvider><App /></AppProvider>);
    let startBtns = await screen.findAllByText("Start Learning", {}, { timeout: 3000 });
    await user.click(startBtns[0]);
    await user.click(screen.getByText("New Player"));
    await user.type(screen.getByPlaceholderText("Username"), "existing");
    await user.click(screen.getByText("Log In"));
    await user.click(screen.getByRole("button", { name: "Profile" }));
    await user.click(await screen.findByText("Log Out"));
    startBtns = await screen.findAllByText("Start Learning", {}, { timeout: 3000 });
    await user.click(startBtns[0]);
    await user.click(await screen.findByText("existing"));
    expect(await screen.findByRole("button", { name: /Relative Clauses: Lesson plan/ })).toBeInTheDocument();
  });
});
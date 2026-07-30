import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { describe, expect, it, vi } from "vitest";
import type { ClozeQuestion } from "../types";
import { ClozeMemorization } from "./BlockBuilderQuestion";

const question: ClozeQuestion = {
  id: "aviation_report_q02",
  type: "cloze",
  q: "All our air _____ packs have _____, so we request rapid descent.",
  qZh: "All our air _____ packs have _____, so we request rapid descent.",
  qEs: "All our air _____ packs have _____, so we request rapid descent.",
  t: "",
  tZh: "",
  tEs: "",
  scenario: "Fill the blanks from memory.",
  scenarioZh: "Fill the blanks from memory.",
  scenarioEs: "Fill the blanks from memory.",
  blanks: [
    { position: 6, word: "conditioning", options: ["conditioning", "layer"] },
    { position: 12, word: "malfunctioned", options: ["freezing", "malfunctioned"] },
  ],
  fullSentence: "All our air conditioning packs have malfunctioned, so we request rapid descent.",
  fullSentenceZh: "All our air conditioning packs have malfunctioned, so we request rapid descent.",
  fullSentenceEs: "All our air conditioning packs have malfunctioned, so we request rapid descent.",
};

describe("ClozeMemorization", () => {
  it("shows the complete sentence before recall", () => {
    render(<ClozeMemorization question={question} language="en" onFirstResult={vi.fn()} onReadyForNext={vi.fn()} />);

    expect(screen.getByText(question.fullSentence)).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Hide words & recall" })).toBeEnabled();
  });

  it("maps placeholders to blanks in order instead of using word positions as character offsets", async () => {
    const user = userEvent.setup();
    render(<ClozeMemorization question={question} language="en" onFirstResult={vi.fn()} onReadyForNext={vi.fn()} />);

    await user.click(screen.getByRole("button", { name: "Hide words & recall" }));

    expect(screen.getByText("All our air")).toBeInTheDocument();
    expect(screen.getByText("packs have")).toBeInTheDocument();
    expect(screen.getByText(", so we request rapid descent.")).toBeInTheDocument();
    expect(screen.queryByText(/_____/)).not.toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Choose a word 1" })).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Choose a word 2" })).toBeInTheDocument();
  });

  it("scores a completed recall round", async () => {
    const user = userEvent.setup();
    const onFirstResult = vi.fn();
    render(<ClozeMemorization question={question} language="en" onFirstResult={onFirstResult} onReadyForNext={vi.fn()} />);

    await user.click(screen.getByRole("button", { name: "Hide words & recall" }));
    await user.click(screen.getByRole("button", { name: "conditioning" }));
    await user.click(screen.getByRole("button", { name: "malfunctioned" }));
    await user.click(screen.getByRole("button", { name: "Check recall" }));

    expect(onFirstResult).toHaveBeenCalledWith(expect.objectContaining({ correct: true, points: 1 }));
    expect(screen.getAllByText("Perfect recall")).toHaveLength(2);
  });
});

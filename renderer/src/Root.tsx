import React, {useEffect, useState} from "react";
import {
  AbsoluteFill,
  delayRender,
  continueRender,
  cancelRender,
  Composition,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import "@fontsource/noto-sans-sc/400.css";

export type CardProps = {
  brand: string;
  title: string;
  subtitle: string;
  accent: string;
  durationSeconds: number;
};
export const MissionCard: React.FC<CardProps> = ({
  brand,
  title,
  subtitle,
  accent,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const unit = width / 1280;
  return (
    <AbsoluteFill
      style={{
        background: "#09111e",
        color: "#eef4fa",
        fontFamily: '"Noto Sans SC",sans-serif',
        overflow: "hidden",
      }}
    >
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(ellipse at 78% 45%, #17304b 0%, transparent 58%)",
        }}
      />
      <svg
        width={width}
        height={height}
        viewBox="0 0 1280 720"
        style={{ position: "absolute" }}
      >
        <g fill="none" stroke={accent} strokeWidth="1" opacity="0.22">
          <ellipse
            cx="1010"
            cy="390"
            rx="280"
            ry="180"
            transform="rotate(-28 1010 390)"
          />
          <ellipse
            cx="1010"
            cy="390"
            rx="330"
            ry="225"
            transform="rotate(-28 1010 390)"
          />
          <circle cx="1010" cy="390" r="110" />
          <path d="M720 390H1280M1010 80V720" />
        </g>
        <g
          transform={`translate(980 ${330 + Math.sin((frame / fps) * 0.6) * 10}) rotate(-22)`}
          stroke={accent}
          fill="#102238"
          strokeWidth="2"
        >
          <rect x="-24" y="-34" width="48" height="68" />
          <path d="M-24 0H-120M24 0H120" />
          <rect x="-145" y="-28" width="108" height="56" />
          <rect x="37" y="-28" width="108" height="56" />
          <path d="M-110-28V28M-74-28V28M73-28V28M109-28V28M0-34V-64M-12-64H12" />
        </g>
      </svg>
      <div
        style={{
          position: "absolute",
          left: 80 * unit,
          top: 64 * unit,
          fontSize: 20 * unit,
          letterSpacing: 4 * unit,
          color: accent,
        }}
      >
        {brand}
      </div>
      <div
        style={{
          position: "absolute",
          left: 80 * unit,
          top: 215 * unit,
          width: 760 * unit,
          opacity: interpolate(frame, [0, 0.7 * fps], [0, 1], {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
          }),
          translate: `0 ${interpolate(frame, [0, 0.7 * fps], [18, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" }) * unit}px`,
        }}
      >
        <div
          style={{
            fontSize: 72 * unit,
            lineHeight: 1.28,
            whiteSpace: "pre-wrap",
            letterSpacing: -2 * unit,
          }}
        >
          {title}
        </div>
        <div
          style={{
            width: 56 * unit,
            height: 3 * unit,
            background: accent,
            marginTop: 34 * unit,
            marginBottom: 24 * unit,
          }}
        />
        <div
          style={{
            fontSize: 28 * unit,
            lineHeight: 1.6,
            color: "#a7bbc9",
            whiteSpace: "pre-wrap",
          }}
        >
          {subtitle}
        </div>
      </div>
      <div
        style={{
          position: "absolute",
          bottom: 58 * unit,
          left: 80 * unit,
          right: 80 * unit,
          display: "flex",
          justifyContent: "space-between",
          fontSize: 14 * unit,
          letterSpacing: 2 * unit,
          color: "#7893a7",
          borderTop: "1px solid #2b4050",
          paddingTop: 20 * unit,
        }}
      >
        <span>航天行业 · 概念排版样例</span>
        <span>BBRAB / MOTION SYSTEM</span>
      </div>
    </AbsoluteFill>
  );
};

type WorkflowProps = {svg: string; variant: string; quality?: string};
// SVG is authored by aerospace_design.py, with escaped customer text and normalized PNG only.
export const WorkflowCard: React.FC<WorkflowProps> = ({svg,quality}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const [fontHandle] = useState(() => delayRender("Load Chinese typography"));
  useEffect(() => { document.fonts.ready.then(() => {
    if (quality === 'brand-v2') {
      const canvas = document.querySelector('[data-brand-canvas] svg');
      if (!canvas) return cancelRender(new Error('Missing design SVG'));
      for (const node of Array.from(canvas.querySelectorAll('text'))) {
        const box = (node as SVGGraphicsElement).getBBox();
        if (box.x < -1 || box.y < -1 || box.x + box.width > 1281 || box.y + box.height > 721) {
          return cancelRender(new Error('Text outside delivery canvas'));
        }
      }
    }
    continueRender(fontHandle);
  }).catch(cancelRender); }, [fontHandle,quality,svg]);
  return <AbsoluteFill style={{background:'#081b2c',overflow:'hidden'}}>
    <div data-brand-canvas style={{width:1280,height:720,opacity:interpolate(frame,[0,.65*fps],[0,1],{extrapolateLeft:'clamp',extrapolateRight:'clamp'})}}
      dangerouslySetInnerHTML={{__html:svg}} />
    <div style={{position:'absolute',left:72,top:614,width:36,height:2,background:'#ffffff55',translate:`${interpolate(frame,[0,6*fps],[0,1100])}px 0`}} />
  </AbsoluteFill>;
};

export const RemotionRoot: React.FC = () => {
  return (
    <>
    <Composition
      id="BbrabMissionCard"
      component={MissionCard}
      durationInFrames={180}
      fps={30}
      width={1280}
      height={720}
      defaultProps={{
        brand: "BBRAB · AEROSPACE",
        title: "星辰之间\n让表达准确抵达",
        subtitle: "固定品牌规范 · 可控文字排版 · 可复用动态模板",
        accent: "#74d8cc",
        durationSeconds: 6,
      }}
      calculateMetadata={({ props }) => ({
        durationInFrames: Math.round(props.durationSeconds * 30),
      })}
    />
    <Composition id="AerospaceWorkflow" component={WorkflowCard} width={1280} height={720} fps={30} durationInFrames={180}
      defaultProps={{svg:'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720"><rect width="1280" height="720" fill="#081b2c"/><text x="80" y="320" fill="white" font-size="72">Aerospace / Selection workflow</text></svg>',variant:'orbit'}} />
    </>
  );
};

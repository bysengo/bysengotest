/* ========================================
   ClubStack - Investment Club Platform
   Main Application Logic
   ======================================== */

// ========== STATE ==========
const state = {
    currentView: 'landing',
    clubs: [],
    filteredClubs: [],
    currentCardIndex: 0,
    likedClubs: JSON.parse(localStorage.getItem('cs_liked') || '[]'),
    myClubs: JSON.parse(localStorage.getItem('cs_my_clubs') || '[]'),
    passedClubs: JSON.parse(localStorage.getItem('cs_passed') || '[]'),
    currentFilter: 'all',
    airtable: JSON.parse(localStorage.getItem('cs_airtable') || 'null'),
};

// ========== SAMPLE DATA (used when Airtable is not connected) ==========
const sampleClubs = [
    {
        id: 'sample-1',
        name: 'Bay Area Growth Fund',
        tagline: 'Investing in tomorrow\'s tech leaders',
        description: 'A collective of Bay Area tech professionals pooling resources to invest in high-growth tech stocks. We meet bi-weekly on Zoom to discuss market trends, analyze opportunities, and vote on new positions. Perfect for those who understand tech and want to ride the next wave.',
        focus: 'stocks',
        strategy: 'Growth',
        minInvestment: 500,
        maxInvestment: 5000,
        maxMembers: 25,
        currentMembers: 18,
        meetingFreq: 'Bi-Weekly',
        format: 'Virtual',
        location: 'San Francisco, CA',
        voting: 'Majority Vote',
        experience: 'Intermediate',
        tags: ['tech', 'large-cap', 'ai-ml'],
        founder: 'Alex Chen',
        founderEmail: 'alex@example.com',
        color: '#6366f1',
        image: '',
        createdAt: '2025-08-15',
    },
    {
        id: 'sample-2',
        name: 'Real Estate Collective',
        tagline: 'Building wealth through property investments',
        description: 'We pool capital to invest in residential and commercial real estate across the Midwest. Members contribute monthly and vote on acquisition targets. Our portfolio includes rental properties, REITs, and real estate syndications. Building generational wealth, one property at a time.',
        focus: 'real-estate',
        strategy: 'Income',
        minInvestment: 1000,
        maxInvestment: 10000,
        maxMembers: 15,
        currentMembers: 12,
        meetingFreq: 'Monthly',
        format: 'Hybrid',
        location: 'Chicago, IL',
        voting: 'Super Majority',
        experience: 'Intermediate',
        tags: ['finance', 'consumer'],
        founder: 'Maria Rodriguez',
        founderEmail: 'maria@example.com',
        color: '#f59e0b',
        image: '',
        createdAt: '2025-06-01',
    },
    {
        id: 'sample-3',
        name: 'Green Impact Fund',
        tagline: 'Profit with purpose: ESG-first investing',
        description: 'An impact-focused investment club targeting companies with strong ESG scores. We believe doing good and doing well aren\'t mutually exclusive. Members research and present sustainable investment opportunities monthly. Our portfolio has outperformed the S&P 500 two years running.',
        focus: 'esg',
        strategy: 'Balanced',
        minInvestment: 250,
        maxInvestment: 3000,
        maxMembers: 30,
        currentMembers: 24,
        meetingFreq: 'Monthly',
        format: 'Virtual',
        location: 'Remote',
        voting: 'Majority Vote',
        experience: 'Beginner Friendly',
        tags: ['sustainable', 'energy', 'international'],
        founder: 'Jordan Okafor',
        founderEmail: 'jordan@example.com',
        color: '#10b981',
        image: '',
        createdAt: '2025-03-10',
    },
    {
        id: 'sample-4',
        name: 'Crypto Pioneers',
        tagline: 'Navigating the digital frontier together',
        description: 'A community of crypto enthusiasts making collective investment decisions in the Web3 space. We cover DeFi protocols, NFT projects, layer-2 solutions, and emerging blockchain ecosystems. High risk, high reward — we educate first and invest second.',
        focus: 'crypto',
        strategy: 'Aggressive',
        minInvestment: 100,
        maxInvestment: 2000,
        maxMembers: 50,
        currentMembers: 38,
        meetingFreq: 'Weekly',
        format: 'Virtual',
        location: 'Remote',
        voting: 'Majority Vote',
        experience: 'Intermediate',
        tags: ['tech', 'ai-ml'],
        founder: 'Sam Nakamura',
        founderEmail: 'sam@example.com',
        color: '#8b5cf6',
        image: '',
        createdAt: '2025-01-20',
    },
    {
        id: 'sample-5',
        name: 'Startup Angels Collective',
        tagline: 'Angel investing for the rest of us',
        description: 'Democratizing angel investing by pooling small checks into startup deals. Members collectively evaluate and invest in seed-stage startups across fintech, healthtech, and climate. We leverage our combined network to source and diligence deals. Min commitment: 12 months.',
        focus: 'startups',
        strategy: 'Aggressive',
        minInvestment: 500,
        maxInvestment: 5000,
        maxMembers: 20,
        currentMembers: 14,
        meetingFreq: 'Bi-Weekly',
        format: 'Hybrid',
        location: 'New York, NY',
        voting: 'Super Majority',
        experience: 'Advanced',
        tags: ['tech', 'healthcare', 'finance'],
        founder: 'Priya Patel',
        founderEmail: 'priya@example.com',
        color: '#ec4899',
        image: '',
        createdAt: '2025-05-12',
    },
    {
        id: 'sample-6',
        name: 'Dividend Dynasty',
        tagline: 'Passive income through smart dividends',
        description: 'Focused exclusively on dividend-paying stocks and income-generating assets. We build and maintain a diversified portfolio of blue-chip dividend aristocrats, REITs, and bonds. Perfect for members seeking steady, reliable income rather than speculative growth.',
        focus: 'stocks',
        strategy: 'Income',
        minInvestment: 200,
        maxInvestment: 3000,
        maxMembers: 40,
        currentMembers: 31,
        meetingFreq: 'Monthly',
        format: 'Virtual',
        location: 'Remote',
        voting: 'Majority Vote',
        experience: 'Beginner Friendly',
        tags: ['finance', 'large-cap', 'etf'],
        founder: 'Robert Kim',
        founderEmail: 'robert@example.com',
        color: '#0ea5e9',
        image: '',
        createdAt: '2024-11-08',
    },
    {
        id: 'sample-7',
        name: 'Women Who Invest',
        tagline: 'Closing the investing gap, together',
        description: 'A supportive community of women learning and investing together. We focus on financial literacy, portfolio construction, and building long-term wealth. Monthly workshops cover everything from reading balance sheets to evaluating ETFs. All experience levels welcome.',
        focus: 'mixed',
        strategy: 'Balanced',
        minInvestment: 100,
        maxInvestment: 2000,
        maxMembers: 35,
        currentMembers: 28,
        meetingFreq: 'Bi-Weekly',
        format: 'Hybrid',
        location: 'Austin, TX',
        voting: 'Majority Vote',
        experience: 'Beginner Friendly',
        tags: ['etf', 'large-cap', 'sustainable'],
        founder: 'Lisa Chang',
        founderEmail: 'lisa@example.com',
        color: '#f43f5e',
        image: '',
        createdAt: '2025-02-14',
    },
    {
        id: 'sample-8',
        name: 'Options Alpha Club',
        tagline: 'Advanced options strategies for consistent returns',
        description: 'For experienced traders looking to generate income through options selling strategies. We run covered calls, iron condors, and credit spreads on a shared portfolio. Weekly meetings to review positions, roll options, and plan new trades. Not for beginners.',
        focus: 'stocks',
        strategy: 'Income',
        minInvestment: 2000,
        maxInvestment: 20000,
        maxMembers: 10,
        currentMembers: 8,
        meetingFreq: 'Weekly',
        format: 'Virtual',
        location: 'Remote',
        voting: 'Fund Manager Decides',
        experience: 'Advanced',
        tags: ['options', 'finance', 'tech'],
        founder: 'David Tran',
        founderEmail: 'david@example.com',
        color: '#14b8a6',
        image: '',
        createdAt: '2025-07-22',
    },
];

// ========== AIRTABLE API ==========
const airtableAPI = {
    get config() {
        return state.airtable;
    },

    get isConnected() {
        return !!(this.config && this.config.token && this.config.baseId);
    },

    get headers() {
        return {
            'Authorization': `Bearer ${this.config.token}`,
            'Content-Type': 'application/json',
        };
    },

    baseUrl(table) {
        return `https://api.airtable.com/v0/${this.config.baseId}/${encodeURIComponent(table)}`;
    },

    async fetchClubs() {
        if (!this.isConnected) return null;
        try {
            const table = this.config.clubsTable || 'Clubs';
            const resp = await fetch(this.baseUrl(table), { headers: this.headers });
            if (!resp.ok) throw new Error(`Airtable error: ${resp.status}`);
            const data = await resp.json();
            return data.records.map(r => mapAirtableToClub(r));
        } catch (err) {
            console.error('Failed to fetch clubs from Airtable:', err);
            showToast('Failed to load clubs from Airtable. Using local data.', 'error');
            return null;
        }
    },

    async createClub(club) {
        if (!this.isConnected) return null;
        try {
            const table = this.config.clubsTable || 'Clubs';
            const resp = await fetch(this.baseUrl(table), {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify({ fields: mapClubToAirtable(club) }),
            });
            if (!resp.ok) {
                const err = await resp.json();
                throw new Error(err.error?.message || `Status ${resp.status}`);
            }
            const data = await resp.json();
            return data.id;
        } catch (err) {
            console.error('Failed to create club in Airtable:', err);
            showToast(`Airtable error: ${err.message}`, 'error');
            return null;
        }
    },

    async submitInterest(interest) {
        if (!this.isConnected) return null;
        try {
            const table = this.config.interestTable || 'Interest';
            const resp = await fetch(this.baseUrl(table), {
                method: 'POST',
                headers: this.headers,
                body: JSON.stringify({
                    fields: {
                        'Club Name': interest.clubName,
                        'Club ID': interest.clubId,
                        'Name': interest.name,
                        'Email': interest.email,
                        'Message': interest.message || '',
                        'Date': new Date().toISOString().split('T')[0],
                    }
                }),
            });
            if (!resp.ok) throw new Error(`Status ${resp.status}`);
            return true;
        } catch (err) {
            console.error('Failed to submit interest to Airtable:', err);
            return false;
        }
    },

    async testConnection() {
        if (!this.isConnected) return false;
        try {
            const table = this.config.clubsTable || 'Clubs';
            const resp = await fetch(`${this.baseUrl(table)}?maxRecords=1`, { headers: this.headers });
            return resp.ok;
        } catch {
            return false;
        }
    }
};

function mapAirtableToClub(record) {
    const f = record.fields;
    return {
        id: record.id,
        name: f['Name'] || f['Club Name'] || '',
        tagline: f['Tagline'] || '',
        description: f['Description'] || '',
        focus: (f['Focus'] || f['Investment Focus'] || 'mixed').toLowerCase(),
        strategy: f['Strategy'] || 'Balanced',
        minInvestment: parseInt(f['Min Investment'] || f['Min Monthly'] || 100),
        maxInvestment: parseInt(f['Max Investment'] || f['Max Monthly'] || 5000),
        maxMembers: parseInt(f['Max Members'] || 25),
        currentMembers: parseInt(f['Current Members'] || 0),
        meetingFreq: f['Meeting Frequency'] || 'Monthly',
        format: f['Format'] || 'Virtual',
        location: f['Location'] || 'Remote',
        voting: f['Voting'] || f['Decision Making'] || 'Majority Vote',
        experience: f['Experience Level'] || 'Beginner Friendly',
        tags: f['Tags'] ? (Array.isArray(f['Tags']) ? f['Tags'] : f['Tags'].split(',').map(t => t.trim())) : [],
        founder: f['Founder'] || f['Founder Name'] || '',
        founderEmail: f['Founder Email'] || '',
        color: f['Color'] || randomColor(),
        image: f['Image'] || (f['Cover Image'] ? f['Cover Image'][0]?.url : '') || '',
        rules: f['Rules'] || '',
        createdAt: record.createdTime?.split('T')[0] || '',
    };
}

function mapClubToAirtable(club) {
    return {
        'Name': club.name,
        'Tagline': club.tagline,
        'Description': club.description,
        'Investment Focus': club.focus,
        'Strategy': club.strategy,
        'Min Investment': club.minInvestment,
        'Max Investment': club.maxInvestment,
        'Max Members': club.maxMembers,
        'Current Members': 1,
        'Meeting Frequency': club.meetingFreq,
        'Format': club.format,
        'Location': club.location,
        'Decision Making': club.voting,
        'Experience Level': club.experience,
        'Tags': club.tags.join(', '),
        'Founder Name': club.founder,
        'Founder Email': club.founderEmail,
        'Color': club.color,
        'Rules': club.rules || '',
    };
}

// ========== INITIALIZATION ==========
document.addEventListener('DOMContentLoaded', () => {
    loadConfig();
    initApp();
});

async function initApp() {
    // Try loading from Airtable first
    const airtableClubs = await airtableAPI.fetchClubs();
    if (airtableClubs && airtableClubs.length > 0) {
        state.clubs = airtableClubs;
        showToast('Loaded clubs from Airtable', 'success');
    } else {
        // Merge sample data with locally created clubs
        state.clubs = [...sampleClubs, ...state.myClubs.filter(c => !sampleClubs.find(s => s.id === c.id))];
    }

    state.filteredClubs = getVisibleClubs();
    animateStats();
    renderCards();
    renderDashboard();
}

function loadConfig() {
    if (state.airtable) {
        const el = document.getElementById;
        const token = document.getElementById('airtableToken');
        const baseId = document.getElementById('airtableBaseId');
        const clubsTable = document.getElementById('airtableClubsTable');
        const interestTable = document.getElementById('airtableInterestTable');
        if (token) token.value = state.airtable.token || '';
        if (baseId) baseId.value = state.airtable.baseId || '';
        if (clubsTable) clubsTable.value = state.airtable.clubsTable || 'Clubs';
        if (interestTable) interestTable.value = state.airtable.interestTable || 'Interest';
    }
}

// ========== VIEW NAVIGATION ==========
function showView(viewName) {
    document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
    const view = document.getElementById(`view-${viewName}`);
    if (view) {
        view.classList.add('active');
        state.currentView = viewName;
        window.scrollTo(0, 0);

        if (viewName === 'discover') {
            state.filteredClubs = getVisibleClubs();
            state.currentCardIndex = 0;
            renderCards();
        }
        if (viewName === 'dashboard') {
            renderDashboard();
        }
    }
}

function toggleMobileMenu() {
    document.getElementById('mobileMenu').classList.toggle('open');
}

// ========== STATS ANIMATION ==========
function animateStats() {
    const totalClubs = state.clubs.length;
    const totalMembers = state.clubs.reduce((sum, c) => sum + (c.currentMembers || 0), 0);
    const totalInvested = state.clubs.reduce((sum, c) => sum + ((c.currentMembers || 0) * (c.minInvestment || 0) * 6), 0);

    animateNumber('stat-clubs', totalClubs);
    animateNumber('stat-members', totalMembers);
    animateNumber('stat-invested', totalInvested, true);
}

function animateNumber(elId, target, isCurrency = false) {
    const el = document.getElementById(elId);
    if (!el) return;
    let current = 0;
    const step = Math.max(1, Math.ceil(target / 40));
    const interval = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = isCurrency ? `$${current.toLocaleString()}` : current.toLocaleString();
        if (current >= target) clearInterval(interval);
    }, 30);
}

// ========== DISCOVER / SWIPE ==========
function getVisibleClubs() {
    const likedSet = new Set(state.likedClubs.map(c => c.id));
    const passedSet = new Set(state.passedClubs);

    return state.clubs.filter(club => {
        if (likedSet.has(club.id) || passedSet.has(club.id)) return false;
        if (state.currentFilter === 'all') return true;
        if (state.currentFilter === 'mixed') return club.focus === 'mixed';
        return club.focus === state.currentFilter;
    });
}

function filterClubs(filter, btn) {
    state.currentFilter = filter;
    document.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    if (btn) btn.classList.add('active');
    state.filteredClubs = getVisibleClubs();
    state.currentCardIndex = 0;
    renderCards();
}

function renderCards() {
    const stack = document.getElementById('cardStack');
    const empty = document.getElementById('emptyState');
    const actions = document.getElementById('swipeActions');

    stack.innerHTML = '';

    const remaining = state.filteredClubs.slice(state.currentCardIndex);

    if (remaining.length === 0) {
        empty.style.display = 'block';
        actions.style.display = 'none';
        return;
    }

    empty.style.display = 'none';
    actions.style.display = 'flex';

    // Render top 3 cards (for stacking effect)
    const toRender = remaining.slice(0, 3).reverse();
    toRender.forEach((club, i) => {
        const actualIndex = toRender.length - 1 - i;
        const card = createCardElement(club, actualIndex);
        stack.appendChild(card);
    });

    // Setup drag on top card
    const topCard = stack.lastElementChild;
    if (topCard) setupSwipeGesture(topCard);
}

function createCardElement(club, stackIndex) {
    const card = document.createElement('div');
    card.className = 'swipe-card';
    card.dataset.clubId = club.id;
    card.style.zIndex = 10 - stackIndex;

    if (stackIndex > 0) {
        card.style.transform = `scale(${1 - stackIndex * 0.04}) translateY(${stackIndex * 12}px)`;
        card.style.opacity = 1 - stackIndex * 0.15;
    }

    const initials = club.name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
    const bgImage = club.image
        ? `<img src="${escapeHtml(club.image)}" alt="${escapeHtml(club.name)}">`
        : `<div style="display:flex;align-items:center;justify-content:center;height:100%;background:linear-gradient(135deg, ${club.color}33, ${club.color}11);">
            <span style="font-size:48px;font-weight:800;color:${club.color};opacity:0.6">${initials}</span>
           </div>`;

    const tagHtml = club.tags.slice(0, 4).map(t =>
        `<span class="card-tag">${escapeHtml(t)}</span>`
    ).join('');

    card.innerHTML = `
        <div class="swipe-indicator like-indicator">Interested</div>
        <div class="swipe-indicator pass-indicator">Pass</div>
        <div class="card-image">
            ${bgImage}
            <div class="card-overlay">
                <div class="club-name">${escapeHtml(club.name)}</div>
                <div class="club-tagline">${escapeHtml(club.tagline || '')}</div>
            </div>
        </div>
        <div class="card-body">
            <p class="club-desc">${escapeHtml(club.description)}</p>
            <div class="card-tags">${tagHtml}</div>
            <div class="card-meta">
                <div class="meta-item">
                    <span class="meta-label">Monthly Min</span>
                    <span class="meta-value">$${club.minInvestment.toLocaleString()}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Members</span>
                    <span class="meta-value">${club.currentMembers || 0} / ${club.maxMembers}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Focus</span>
                    <span class="meta-value">${capitalize(club.focus)}</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Experience</span>
                    <span class="meta-value">${club.experience}</span>
                </div>
            </div>
        </div>
    `;

    return card;
}

// ========== SWIPE GESTURE ==========
function setupSwipeGesture(card) {
    let startX = 0, startY = 0, currentX = 0, isDragging = false;

    function onStart(e) {
        isDragging = true;
        startX = e.type === 'mousedown' ? e.clientX : e.touches[0].clientX;
        startY = e.type === 'mousedown' ? e.clientY : e.touches[0].clientY;
        card.style.transition = 'none';
    }

    function onMove(e) {
        if (!isDragging) return;
        const x = e.type === 'mousemove' ? e.clientX : e.touches[0].clientX;
        currentX = x - startX;
        const rotate = currentX * 0.08;
        card.style.transform = `translateX(${currentX}px) rotate(${rotate}deg)`;

        // Show indicators
        const likeInd = card.querySelector('.like-indicator');
        const passInd = card.querySelector('.pass-indicator');
        if (currentX > 30) {
            likeInd.style.opacity = Math.min(1, (currentX - 30) / 80);
            passInd.style.opacity = 0;
        } else if (currentX < -30) {
            passInd.style.opacity = Math.min(1, (Math.abs(currentX) - 30) / 80);
            likeInd.style.opacity = 0;
        } else {
            likeInd.style.opacity = 0;
            passInd.style.opacity = 0;
        }
    }

    function onEnd() {
        if (!isDragging) return;
        isDragging = false;
        card.style.transition = 'transform 0.5s ease, opacity 0.5s ease';

        if (currentX > 100) {
            animateCardOut(card, 'right');
        } else if (currentX < -100) {
            animateCardOut(card, 'left');
        } else {
            card.style.transform = '';
            card.querySelector('.like-indicator').style.opacity = 0;
            card.querySelector('.pass-indicator').style.opacity = 0;
        }
        currentX = 0;
    }

    card.addEventListener('mousedown', onStart);
    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onEnd);
    card.addEventListener('touchstart', onStart, { passive: true });
    card.addEventListener('touchmove', onMove, { passive: true });
    card.addEventListener('touchend', onEnd);
}

function animateCardOut(card, direction) {
    const xOut = direction === 'right' ? 600 : -600;
    card.style.transform = `translateX(${xOut}px) rotate(${direction === 'right' ? 30 : -30}deg)`;
    card.style.opacity = '0';

    const club = state.filteredClubs[state.currentCardIndex];
    if (direction === 'right' && club) {
        // Liked
        if (!state.likedClubs.find(c => c.id === club.id)) {
            state.likedClubs.push(club);
            localStorage.setItem('cs_liked', JSON.stringify(state.likedClubs));
        }
        showToast(`Added "${club.name}" to your interested list`, 'success');
    } else if (direction === 'left' && club) {
        // Passed
        if (!state.passedClubs.includes(club.id)) {
            state.passedClubs.push(club.id);
            localStorage.setItem('cs_passed', JSON.stringify(state.passedClubs));
        }
    }

    setTimeout(() => {
        state.currentCardIndex++;
        renderCards();
    }, 400);
}

function swipeCard(direction) {
    const stack = document.getElementById('cardStack');
    const topCard = stack.lastElementChild;
    if (!topCard) return;
    topCard.style.transition = 'transform 0.5s ease, opacity 0.5s ease';
    animateCardOut(topCard, direction);
}

function resetCards() {
    state.passedClubs = [];
    state.likedClubs = [];
    localStorage.setItem('cs_passed', '[]');
    localStorage.setItem('cs_liked', '[]');
    state.filteredClubs = getVisibleClubs();
    state.currentCardIndex = 0;
    renderCards();
    renderDashboard();
}

// ========== CLUB DETAIL MODAL ==========
function showCardDetail() {
    const club = state.filteredClubs[state.currentCardIndex];
    if (!club) return;
    showClubDetail(club);
}

function showClubDetail(club) {
    const body = document.getElementById('clubDetailBody');
    body.innerHTML = `
        <div class="detail-header">
            <h2>${escapeHtml(club.name)}</h2>
            <p class="detail-tagline">${escapeHtml(club.tagline || '')}</p>
        </div>
        <div class="detail-section">
            <h4>About</h4>
            <p>${escapeHtml(club.description)}</p>
        </div>
        <div class="detail-grid">
            <div class="detail-stat">
                <div class="ds-label">Monthly Min</div>
                <div class="ds-value">$${club.minInvestment.toLocaleString()}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Monthly Max</div>
                <div class="ds-value">$${(club.maxInvestment || club.minInvestment * 10).toLocaleString()}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Members</div>
                <div class="ds-value">${club.currentMembers || 0} / ${club.maxMembers}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Focus</div>
                <div class="ds-value">${capitalize(club.focus)}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Strategy</div>
                <div class="ds-value">${club.strategy}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Meetings</div>
                <div class="ds-value">${club.meetingFreq}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Format</div>
                <div class="ds-value">${club.format}</div>
            </div>
            <div class="detail-stat">
                <div class="ds-label">Decision Making</div>
                <div class="ds-value">${club.voting}</div>
            </div>
        </div>
        ${club.rules ? `<div class="detail-section"><h4>Rules & Requirements</h4><p>${escapeHtml(club.rules)}</p></div>` : ''}
        <div class="detail-section">
            <h4>Experience Level</h4>
            <p>${club.experience}</p>
        </div>
        <div class="detail-section">
            <h4>Location</h4>
            <p>${escapeHtml(club.location || 'Remote')}</p>
        </div>
        <div class="detail-section">
            <h4>Founded By</h4>
            <p>${escapeHtml(club.founder)}</p>
        </div>
        <div class="card-tags" style="margin-bottom:0">
            ${club.tags.map(t => `<span class="card-tag">${escapeHtml(t)}</span>`).join('')}
        </div>
        <div class="detail-actions">
            <button class="btn btn-primary btn-lg btn-full" onclick="openJoinModal('${club.id}')">Express Interest</button>
            <button class="btn btn-outline" onclick="closeModal('clubDetailModal')">Close</button>
        </div>
    `;
    openModal('clubDetailModal');
}

// ========== JOIN / INTEREST ==========
let joiningClubId = null;

function openJoinModal(clubId) {
    joiningClubId = clubId;
    const club = state.clubs.find(c => c.id === clubId);
    if (club) {
        document.getElementById('joinClubName').textContent = `Joining: ${club.name}`;
    }
    closeModal('clubDetailModal');
    openModal('joinModal');
}

async function submitInterest(e) {
    e.preventDefault();
    const club = state.clubs.find(c => c.id === joiningClubId);
    if (!club) return;

    const interest = {
        clubId: joiningClubId,
        clubName: club.name,
        name: document.getElementById('joinName').value,
        email: document.getElementById('joinEmail').value,
        message: document.getElementById('joinMessage').value,
    };

    // Try Airtable
    await airtableAPI.submitInterest(interest);

    // Add to liked if not already there
    if (!state.likedClubs.find(c => c.id === club.id)) {
        state.likedClubs.push(club);
        localStorage.setItem('cs_liked', JSON.stringify(state.likedClubs));
    }

    closeModal('joinModal');
    showToast(`Interest sent to ${club.name}! The organizer will reach out.`, 'success');
    document.getElementById('joinForm').reset();
    renderDashboard();
}

// ========== CREATE CLUB FORM ==========
let currentStep = 1;

function nextStep(step) {
    // Validate current step
    const currentStepEl = document.querySelector(`.form-step[data-step="${currentStep}"]`);
    const requiredFields = currentStepEl.querySelectorAll('[required]');
    let valid = true;
    requiredFields.forEach(f => {
        if (!f.value.trim()) {
            f.style.borderColor = 'var(--red)';
            valid = false;
            f.addEventListener('input', () => { f.style.borderColor = ''; }, { once: true });
        }
    });
    if (!valid) {
        showToast('Please fill in all required fields', 'error');
        return;
    }

    if (step === 4) {
        renderReview();
    }

    currentStep = step;
    document.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    document.querySelector(`.form-step[data-step="${step}"]`).classList.add('active');

    document.querySelectorAll('.progress-step').forEach(s => {
        const stepNum = parseInt(s.dataset.step);
        s.classList.remove('active', 'completed');
        if (stepNum === step) s.classList.add('active');
        if (stepNum < step) s.classList.add('completed');
    });
}

function prevStep(step) {
    currentStep = step;
    document.querySelectorAll('.form-step').forEach(s => s.classList.remove('active'));
    document.querySelector(`.form-step[data-step="${step}"]`).classList.add('active');

    document.querySelectorAll('.progress-step').forEach(s => {
        const stepNum = parseInt(s.dataset.step);
        s.classList.remove('active', 'completed');
        if (stepNum === step) s.classList.add('active');
        if (stepNum < step) s.classList.add('completed');
    });
}

function renderReview() {
    const card = document.getElementById('reviewCard');
    const tags = Array.from(document.querySelectorAll('.tag-grid input:checked')).map(c => c.value);

    card.innerHTML = `
        <h3>${escapeHtml(document.getElementById('clubName').value)}</h3>
        <p class="review-tagline">${escapeHtml(document.getElementById('clubTagline').value || 'No tagline')}</p>
        <p class="review-desc">${escapeHtml(document.getElementById('clubDescription').value)}</p>
        <div class="card-tags" style="margin-bottom:16px;">
            ${tags.map(t => `<span class="card-tag">${escapeHtml(t)}</span>`).join('') || '<span style="color:var(--text-muted)">No tags selected</span>'}
        </div>
        <div class="review-grid">
            <div class="review-item">
                <div class="ri-label">Focus</div>
                <div class="ri-value">${capitalize(document.getElementById('clubFocus').value || 'Mixed')}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Strategy</div>
                <div class="ri-value">${document.getElementById('clubStrategy').value || 'Growth'}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Min Monthly</div>
                <div class="ri-value">$${parseInt(document.getElementById('clubMinInvestment').value || 0).toLocaleString()}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Max Members</div>
                <div class="ri-value">${document.getElementById('clubMaxMembers').value || '25'}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Meetings</div>
                <div class="ri-value">${capitalize(document.getElementById('clubMeetingFreq').value)}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Format</div>
                <div class="ri-value">${capitalize(document.getElementById('clubFormat').value)}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Founder</div>
                <div class="ri-value">${escapeHtml(document.getElementById('founderName').value)}</div>
            </div>
            <div class="review-item">
                <div class="ri-label">Experience</div>
                <div class="ri-value">${capitalize(document.getElementById('clubExperience').value)}</div>
            </div>
        </div>
    `;
}

async function submitClub(e) {
    e.preventDefault();
    const btn = document.getElementById('publishBtn');
    btn.disabled = true;
    btn.textContent = 'Publishing...';

    const tags = Array.from(document.querySelectorAll('.tag-grid input:checked')).map(c => c.value);

    const club = {
        id: 'local-' + Date.now(),
        name: document.getElementById('clubName').value,
        tagline: document.getElementById('clubTagline').value,
        description: document.getElementById('clubDescription').value,
        focus: document.getElementById('clubFocus').value,
        strategy: document.getElementById('clubStrategy').value,
        minInvestment: parseInt(document.getElementById('clubMinInvestment').value),
        maxInvestment: parseInt(document.getElementById('clubMaxInvestment').value || 0),
        maxMembers: parseInt(document.getElementById('clubMaxMembers').value),
        currentMembers: 1,
        meetingFreq: capitalize(document.getElementById('clubMeetingFreq').value),
        format: capitalize(document.getElementById('clubFormat').value),
        location: document.getElementById('clubLocation').value || 'Remote',
        voting: document.getElementById('clubVoting').selectedOptions[0].text,
        experience: document.getElementById('clubExperience').selectedOptions[0].text,
        tags: tags,
        founder: document.getElementById('founderName').value,
        founderEmail: document.getElementById('founderEmail').value,
        rules: document.getElementById('clubRules').value,
        color: randomColor(),
        image: document.getElementById('clubImage').value || '',
        createdAt: new Date().toISOString().split('T')[0],
    };

    // Try saving to Airtable
    const airtableId = await airtableAPI.createClub(club);
    if (airtableId) {
        club.id = airtableId;
        showToast('Club saved to Airtable!', 'success');
    }

    // Save locally
    state.myClubs.push(club);
    state.clubs.push(club);
    localStorage.setItem('cs_my_clubs', JSON.stringify(state.myClubs));

    // Show success
    document.getElementById('createClubForm').style.display = 'none';
    document.querySelector('.form-progress').style.display = 'none';
    document.getElementById('formSuccess').style.display = 'block';

    btn.disabled = false;
    btn.textContent = 'Publish to ClubStack';
}

// ========== DASHBOARD ==========
function renderDashboard() {
    // My Clubs
    const myList = document.getElementById('myClubsList');
    const myEmpty = document.getElementById('myClubsEmpty');

    if (state.myClubs.length > 0) {
        myEmpty.style.display = 'none';
        myList.innerHTML = state.myClubs.map(club => {
            const initials = club.name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
            return `
                <div class="dash-card">
                    <div class="dash-card-avatar" style="background:${club.color}">${initials}</div>
                    <div class="dash-card-info">
                        <h4>${escapeHtml(club.name)}</h4>
                        <p>${club.currentMembers || 1} member${(club.currentMembers || 1) === 1 ? '' : 's'} &bull; ${capitalize(club.focus)}</p>
                    </div>
                    <div class="dash-card-actions">
                        <button class="btn btn-ghost btn-sm" onclick='showClubDetail(${JSON.stringify(club).replace(/'/g, "\\'")})'>View</button>
                    </div>
                </div>
            `;
        }).join('');
    } else {
        myEmpty.style.display = 'block';
        myList.innerHTML = '';
    }

    // Interested
    const intList = document.getElementById('interestedList');
    const intEmpty = document.getElementById('interestedEmpty');

    if (state.likedClubs.length > 0) {
        intEmpty.style.display = 'none';
        intList.innerHTML = state.likedClubs.map(club => {
            const initials = club.name.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();
            return `
                <div class="dash-card">
                    <div class="dash-card-avatar" style="background:${club.color}">${initials}</div>
                    <div class="dash-card-info">
                        <h4>${escapeHtml(club.name)}</h4>
                        <p>$${club.minInvestment.toLocaleString()}/mo min &bull; ${capitalize(club.focus)}</p>
                    </div>
                    <div class="dash-card-actions">
                        <button class="btn btn-ghost btn-sm" onclick='showClubDetail(${JSON.stringify(club).replace(/'/g, "\\'")})'>Details</button>
                        <button class="btn btn-primary btn-sm" onclick="openJoinModal('${club.id}')">Join</button>
                    </div>
                </div>
            `;
        }).join('');
    } else {
        intEmpty.style.display = 'block';
        intList.innerHTML = '';
    }
}

function switchDashTab(panel, btn) {
    document.querySelectorAll('.dash-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.dash-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(`panel-${panel}`).classList.add('active');
}

// ========== AIRTABLE CONFIG ==========
async function saveAirtableConfig(e) {
    e.preventDefault();
    const config = {
        token: document.getElementById('airtableToken').value,
        baseId: document.getElementById('airtableBaseId').value,
        clubsTable: document.getElementById('airtableClubsTable').value || 'Clubs',
        interestTable: document.getElementById('airtableInterestTable').value || 'Interest',
    };

    state.airtable = config;
    localStorage.setItem('cs_airtable', JSON.stringify(config));

    const status = document.getElementById('configStatus');
    status.textContent = 'Testing connection...';
    status.className = 'config-status info';
    status.style.display = 'block';

    const ok = await airtableAPI.testConnection();
    if (ok) {
        status.textContent = 'Connected to Airtable successfully!';
        status.className = 'config-status success';
        showToast('Airtable connected!', 'success');
        // Reload clubs
        const airtableClubs = await airtableAPI.fetchClubs();
        if (airtableClubs && airtableClubs.length > 0) {
            state.clubs = airtableClubs;
            state.filteredClubs = getVisibleClubs();
            renderCards();
            animateStats();
        }
    } else {
        status.textContent = 'Connection failed. Check your token and base ID.';
        status.className = 'config-status error';
    }
}

// ========== MODALS ==========
function openModal(id) {
    document.getElementById(id).classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeModal(id) {
    document.getElementById(id).classList.remove('open');
    document.body.style.overflow = '';
}

// Close modals on overlay click
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('modal-overlay')) {
        e.target.classList.remove('open');
        document.body.style.overflow = '';
    }
});

// ========== TOAST ==========
function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3500);
}

// ========== UTILITIES ==========
function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

function capitalize(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).replace(/-/g, ' ');
}

function randomColor() {
    const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b', '#10b981', '#0ea5e9', '#14b8a6'];
    return colors[Math.floor(Math.random() * colors.length)];
}

// ========== KEYBOARD SHORTCUTS ==========
document.addEventListener('keydown', (e) => {
    if (state.currentView !== 'discover') return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

    if (e.key === 'ArrowLeft') {
        swipeCard('left');
    } else if (e.key === 'ArrowRight') {
        swipeCard('right');
    } else if (e.key === 'ArrowUp' || e.key === ' ') {
        e.preventDefault();
        showCardDetail();
    }
});
